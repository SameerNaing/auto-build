import os

from settings import BASE_DIR


__all__ = ["delete_log_file"]


def delete_log_file(branch: str, commit_hash: str):
    """Function to delete log file from local after uploaded to google drive

    Args:
        branch (str): branch name
        commit_hash (str): commit hash
    """
    file = os.path.join(BASE_DIR, "exports",
                        "logs", branch.replace("/", "-"), f"{commit_hash}.log")

    if os.path.exists(file):
        os.remove(file)
