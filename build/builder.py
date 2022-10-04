from logging import Logger
from datetime import datetime
import multiprocessing

from common.constants import DRIVE_LOG_FILE, DRIVE_APK_FILE, DONE
import db.helpers as db_helpers
from db.core import get_session
from db.models import BuildQueueModel
from git.core.actions import pull, checkout, reset, remove_new_files
from system.core import replace_env, delete_log_file
from google.helpers import send_building_message, send_build_done_message, upload_log_drive

from .helper import ios_build, android_build
from .core import yarn_install, copy_mmtools
from .utils import get_logger


def builder(queue_id: int):
    with get_session() as session:
        queue: BuildQueueModel = session.query(
            BuildQueueModel).get(queue_id)

        checkout(queue.branch_name)
        process = pull(branch=queue.branch_name)
        queue.process_pid = process.pid
        session.commit()
        _, _ = process.communicate()

        if process.returncode != 0:
            return

        logger: Logger = get_logger(
            commit_hash=queue.commit_hash, branch_name=queue.branch_name)

        logger.info(f"Building {queue.commit_hash} | {queue.branch_name}")

        process = multiprocessing.current_process()
        queue.multiprocess_pid = process.pid
        session.commit()

        queue.build_started_at = datetime.now()
        session.commit()

        send_building_message(queue)
        logger.info(f"Building message Sent")

        replaced_env = replace_env(queue.branch_name)
        logger.info(f".env file content replaced with {replaced_env}")

        yarn_install(session, queue.commit_hash)
        logger.info("yarn install done.")

        copy_mmtools()
        logger.info("mmtools added.")

        if queue.build_ios == 1 and queue.ios_building_status != DONE:
            ios_build(session, queue, logger)

        if queue.build_android == 1 and queue.android_building_status != DONE:
            android_build(session, queue, logger)

        logger.info("********** Finished **********")

        file_id, log_share_url = upload_log_drive(
            queue.commit_hash, queue.branch_name)

        delete_log_file(branch=queue.branch_name,
                        commit_hash=queue.commit_hash)

        db_helpers.save_drive_info(session, file_id, queue.commit_hash,
                                   share_url=log_share_url, file_type=DRIVE_LOG_FILE)

        apk_share_url = db_helpers.get_drive_share_url(
            session, queue.commit_hash, DRIVE_APK_FILE)

        send_build_done_message(queue, apk_share_url, log_share_url)

        reset()
        remove_new_files()

        session.delete(queue)
        session.commit()
