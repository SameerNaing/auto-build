import os

from settings import BASE_DIR

__all__ = ["delete_apk_file"]


def delete_apk_file(branch: str, commit_hash: str):
    """Function to delete local apk file after uploaded to google drive

    Args:
        branch (str): branch name
        commit_hash (str): commit hash
    """
    file = os.path.join(BASE_DIR, "exports",
                        "APKs", branch.replace("/", "-"), f"{commit_hash}.apk")

    if os.path.exists(file):
        os.remove(file)
