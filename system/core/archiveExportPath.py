import os
from settings import BASE_DIR


__all__ = ["get_archive_export_path"]


def get_archive_export_path(branch_name: str, commit_hash: str, archive_file_name: str) -> str:
    """Function to get archive export path

    Args:
        branch_name (str): branch name
        commit_hash (str): commit hash
        archive_file_name (str): archive file name

    Returns:
        str: archive export path
    """
    return os.path.join(
        BASE_DIR,
        "exports",
        "Archives",
        branch_name.replace("/", "-"),
        commit_hash,
        archive_file_name
    )
