import os

from settings import BASE_DIR


__all__ = ["create_log_file_dir"]


def create_log_file_dir(branch_name: str):
    """Function to create dir for log file

    Args:
        branch_name (str): branch name
    """
    log_dir = os.path.join(BASE_DIR, "exports", "logs",
                           branch_name.replace("/", "-"))

    if os.path.exists(log_dir):
        return

    os.makedirs(log_dir)
