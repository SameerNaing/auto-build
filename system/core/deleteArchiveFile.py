import os
import shutil

from settings import BASE_DIR

__all__ = ["delete_archive_file"]


def delete_archive_file(branch: str, commit_hash: str):
    """Function to delete ios archive file from local after uploaded to testflight

    Args:
        branch (str): branch name
        commit_hash (str): commit hash
    """
    folder = os.path.join(BASE_DIR, "exports", "Archives",
                          branch.replace("/", "-"), commit_hash)

    if os.path.exists(folder):
        shutil.rmtree(folder)
