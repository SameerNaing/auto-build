import os

from settings import BASE_DIR


__all__ = ["get_log_path"]


def get_log_path(commit_hash: str, branch_name: str) -> str:
    """Function to create log file store path

    Args:
        commit_hash (str): commit hash
        branch_name (str): branch name

    Returns:
        str: log file store path
    """
    _, branch = branch_name.split("/")

    path = os.path.join(BASE_DIR, "exports", "logs",
                        branch, f'{commit_hash}.log')
    os.makedirs(os.path.dirname(path), exist_ok=True)

    return path
