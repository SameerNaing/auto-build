from typing import Union
from subprocess import Popen
from logging import Logger

from common.constants import DRIVE_APK_FILE, BUILDING, PREPARING, DONE, FAILED, UPLOADING
from db.models import BuildQueueModel
import db.helpers as db_helper
from settings import BASE_DIR
from system.core import rename_generated_apk, move_apk_file, delete_apk_file, check_apk_exists
from google.helpers import upload_apk_drive

from .. import core as build_core


__all__ = ["android_build"]


def android_build(session, queue: BuildQueueModel, logger: Logger):
    metro_process: Union[None, Popen] = None
    try:
        if not check_apk_exists(queue.branch_name, queue.commit_hash):
            logger.info(
                f"********  Building Android {queue.android_version_code}({queue.android_version_number}) ********")

            queue.android_building_status = PREPARING
            session.commit()

            logger.info("Build Bundle Android Running....")
            build_core.build_bundle_android(session, queue.commit_hash)
            logger.info("Build Bundle Android Done")

            build_core.remove_assets(session, queue.commit_hash)
            logger.info("Removed assests")

            metro_process = build_core.start_metro_server(
                session, queue.commit_hash)
            logger.info("Metro server started")

            logger.info("Cleaning project ...")
            build_core.clean_project(session=session, commit_hash=queue.commit_hash,
                                     versionCode=queue.android_version_code, versionNumber=queue.android_version_number)
            logger.info("Project Cleaned.")

            queue.android_building_status = BUILDING
            session.commit()

            logger.info("Generating Apk ...")
            build_core.build_apk(session=session, commit_hash=queue.commit_hash,
                                 versionCode=queue.android_version_code, versionNumber=queue.android_version_number)
            logger.info("Apk Generated Successfully.")

            metro_process.terminate()
            logger.info("Metro server stopped")

            new_filename = rename_generated_apk(queue.commit_hash)
            logger.info("APK file renamed.")

            file_path = move_apk_file(queue.branch_name, new_filename)
            logger.info("APK File moved to autobuild/export dir.")

        queue.android_building_status = UPLOADING
        session.commit()

        file_id, share_url = upload_apk_drive(
            queue.commit_hash, queue.branch_name, file_path)
        logger.info("Uploaded Apk to Google Drive.")

        delete_apk_file(branch=queue.branch_name,
                        commit_hash=queue.commit_hash)

        logger.info("Local Apk file deleted.")

        queue.android_building_status = DONE
        session.commit()

        db_helper.save_drive_info(session=session, file_id=file_id,
                                  commit_hash=queue.commit_hash, share_url=share_url, file_type=DRIVE_APK_FILE)
        logger.info("Done")
    except Exception as e:
        if metro_process != None:
            metro_process.terminate()

        queue.android_building_status = FAILED
        session.commit()
        logger.error("Android Build Failed")
        logger.error(e)
