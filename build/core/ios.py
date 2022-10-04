from sqlalchemy.orm import Session

from system.decorators import change_rn_ios_dir
from system.core import get_archive_export_path

from ..utils.saveRunProcess import save_run_process


__all__ = ["pod_install", "archive", "upload_archive"]


@change_rn_ios_dir
def pod_install(session: Session, commit_hash: str):
    """Spawn "pod install" subporcess and saves the subprocess
       process id (pid) in database.

    Args:
        session (Session): sqlalchemy orm session
        commit_hash (str): commit hash to store the pid
    """
    save_run_process(session=session, process_command=[
                     "pod", "install"], commit_hash=commit_hash, is_metro_server=False)


@change_rn_ios_dir
def archive(session: Session, commit_hash: str, scheme: str, archive_file_name: str, branch: str):
    """Spawn xcode archive process for archiving the ios app

    Args:
        session (Session): sqlalchemy orm session
        commit_hash (str): commit hash to store the pid
        scheme (str): Archive scheme name
        archive_file_name (str): The output archive file name
        branch (str): branch name
    """
    export_path = get_archive_export_path(
        branch, commit_hash, archive_file_name)

    command = ["xcodebuild", "-workspace", "Flymya.xcworkspace",
               "-scheme", scheme, "-destination", "generic/platform=IOS",
               "-configuration", "Release", "-xcconfig", "archiveConfig.xcconfig", "archive",
               "-archivePath", export_path]

    save_run_process(session=session, process_command=command,
                     commit_hash=commit_hash, is_metro_server=False)


@change_rn_ios_dir
def upload_archive(session: Session, commit_hash: str, archive_file_name: str, branch: str):
    """Spawn archive upload to testflight process

    Args:
        session (Session): sqlalchemy orm session
        commit_hash (str): commit hash to store the pid
        archive_file_name (str): archived file name
        branch (str): branch name
    """

    archive_path = get_archive_export_path(
        branch, commit_hash, archive_file_name)

    export_path = "/".join(archive_path.split("/")[:-1])

    command = ["xcodebuild", "-exportArchive", "-archivePath", archive_path,
               "-exportOptionsPlist", "exportOptions.plist", "-exportPath", export_path]

    save_run_process(session=session, process_command=command,
                     commit_hash=commit_hash, is_metro_server=False)
