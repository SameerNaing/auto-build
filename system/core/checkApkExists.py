import os

from settings import BASE_DIR

__all__ = ["check_apk_exists"]


def check_apk_exists(branch_name: str, commit_hash: str) -> bool:
    """Function to check if the apk file exists in exports dir

    Args:
        branch_name (str): branch name
        commit_hash (str): commit hash

    Returns:
        bool: return True if file exists, else False
    """
    file = os.path.join(BASE_DIR, "exports", "APKs",
                        branch_name.replace("/", "-"), f"{commit_hash}.apk")

    return os.path.exists(file)
