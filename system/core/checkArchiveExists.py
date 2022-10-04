import os

from settings import BASE_DIR

__all__ = ["check_archive_exists"]


def check_archive_exists(branch_name: str, commit_hash: str) -> bool:
    """Function to check ios archive file exists in exports dir

    Args:
        branch_name (str): branch name
        commit_hash (str): commit hash

    Returns:
        bool: returns True if file exists else False
    """
    folder = os.path.join(BASE_DIR, "exports", "Archives",
                          branch_name.replace("/", "-"), commit_hash)

    return os.path.exists(folder)
