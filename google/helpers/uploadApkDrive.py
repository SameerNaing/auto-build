from typing import Tuple

from settings import APK_FOLDER_BRANCH_MAP

from ..core import upload_file_drive, share_file_link_drive


__all__ = ["upload_apk_drive"]


def upload_apk_drive(commit_hash: str, branch_name: str, apk_file_path: str) -> Tuple[str, str]:
    """Function to upload apk file to google drive

    Args:
        commit_hash (str): commit hash
        branch_name (str): branch name
        apk_file_path (str): local apk file path

    Returns:
        Tuple[str, str]: google drive file id and public share url
    """
    folder_id = APK_FOLDER_BRANCH_MAP.get(branch_name, "release")
    file_id = upload_file_drive(
        parent_folder=folder_id,
        meta_file_name=f"{commit_hash}.apk",
        mimetype="application/vnd.android.package-archive",
        upload_file_path=apk_file_path
    )

    share_link = share_file_link_drive(file_id)

    return file_id, share_link
