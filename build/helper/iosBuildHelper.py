from typing import Union
from logging import Logger
from subprocess import Popen

from system.core import change_archive_config, remove_pods, delete_archive_file, check_archive_exists
from db.models import BuildQueueModel
from common.constants import DONE, FAILED, PREPARING, BUILDING, UPLOADING

from .. import utils as build_utils
from .. import core as build_core


__all__ = ["ios_build"]


def ios_build(session, queue: BuildQueueModel, logger: Logger):
    metro_process: Union[None, Popen] = None

    try:
        scheme = build_utils.get_scheme_name(queue.branch_name)
        archive_name = build_utils.get_archive_name(queue.branch_name)

        if not check_archive_exists(queue.branch_name, queue.commit_hash):
            logger.info(
                f"********  Building IOS {queue.ios_version_number}({queue.ios_build_number}) ********")
            logger.info(
                f"Scheme : {scheme} | Archive file name : {archive_name}")

            queue.ios_building_status = PREPARING
            session.commit()

            change_archive_config(queue.ios_version_number,
                                  queue.ios_build_number)
            logger.info(
                f"Version number : {queue.ios_version_number} | Build number : { queue.ios_build_number} added to config file.")

            remove_pods()
            logger.info("Pods and Podfile.lock removed")

            logger.info("Pods installing...")
            build_core.pod_install(session, queue.commit_hash)
            logger.info("Pods installed")

            metro_process = build_core.start_metro_server(
                session, queue.commit_hash)

            logger.info("Metro server started")

            queue.ios_building_status = BUILDING
            session.commit()

            logger.info("Archiving...")
            build_core.archive(session, queue.commit_hash,
                               scheme, archive_name, queue.branch_name)
            logger.info("Archived Successfully")

            metro_process.terminate()
            logger.info("Metro server process stopped")

        queue.ios_building_status = UPLOADING
        session.commit()

        logger.info("Uploading to testflight...")
        build_core.upload_archive(
            session, queue.commit_hash, archive_name, queue.branch_name)
        logger.info("Uploaded to testflight Successfully")

        queue.ios_building_status = DONE
        session.commit()

        delete_archive_file(queue.branch_name, queue.commit_hash)

    except Exception as e:
        if metro_process != None:
            metro_process.terminate()

        queue.ios_building_status = FAILED
        logger.error("IOS Build Failed")
        logger.error(e)
