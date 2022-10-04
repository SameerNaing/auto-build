import subprocess
from typing import List


def common_subprocess_handler(command: List[str]) -> str:
    """Function to handle spawn process

    Args:
        command (List[str]): subprocess command

    Raises:
        Exception: if the subprocess return code is not 0

    Returns:
        str: the output string from subprocess
    """
    process = subprocess.Popen(
        command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    out, err = process.communicate()

    if process.returncode != 0:
        raise Exception(err.decode("utf-8"))

    return out
