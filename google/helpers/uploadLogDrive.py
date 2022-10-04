import os
from typing import Tuple

from settings import BASE_DIR, LOGS_FOLDER_BRANCH_MAP

from ..core import upload_file_drive, share_file_link_drive


__all__ = ["upload_log_drive"]


def upload_log_drive(commit_hash: str, branch_name: str) -> Tuple[str, str]:
    """Function to upload apk file to google drive

    Args:
        commit_hash (str): commit hash
        branch_name (str): branch name
        apk_file_path (str): local log file path

    Returns:
        Tuple[str, str]: google drive file id and public share url
    """
    log_file_path = os.path.join(BASE_DIR, "exports", "logs", branch_name.replace(
        "/", "-"), f"{commit_hash}.log")
    folder_id = LOGS_FOLDER_BRANCH_MAP.get(branch_name, "release")
    file_id = upload_file_drive(
        parent_folder=folder_id,
        meta_file_name=f"{commit_hash}.log",
        mimetype="text/plain",
        upload_file_path=log_file_path
    )

    share_link = share_file_link_drive(file_id)

    return file_id, share_link
