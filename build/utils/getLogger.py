import os
import logging
from logging import Logger

from settings import BASE_DIR
from system.core import create_log_file_dir


__all__ = ["get_logger"]


def get_logger(commit_hash: str, branch_name: str) -> Logger:
    """Function to get logger instance for logging

    Args:
        commit_hash (str): commit hash to store the log file
        branch_name (str): branch name to store the log file

    Returns:
        Logger: logger instance for logging
    """
    create_log_file_dir(branch_name)

    LOG_DIR = os.path.join(BASE_DIR, "exports",
                           "logs", branch_name.replace("/", '-'), f"{commit_hash}.log")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                  '%m-%d-%Y %I:%M:%S %p')

    file_handler = logging.FileHandler(LOG_DIR)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
