import subprocess
from sys import stdout
from system.decorators import change_rn_dir
from common.process import common_subprocess_handler


@change_rn_dir
def checkout(branch_name: str) -> bool:
    """Function to checkout branch

    Args:
        branch_name (str): name of the branch to checkout

    Raises:
        Exception: if the checkout command get some error

    Returns:
        bool: Returns True if checkout is success
    """

    common_subprocess_handler(["git", "checkout", branch_name])
    return True


@change_rn_dir
def fetch_origin() -> bool:
    """Function to Fetch update from origin

    Raises:
        Exception: if there 

    Returns:
        bool: _description_
    """

    common_subprocess_handler(["git", "fetch", "origin"])

    return True


@change_rn_dir
def pull(branch) -> subprocess.Popen:
    """Function to pull data from remote branch

    Raises:
        Exception: If error occure in pulling code

    Returns:
        Popen: popen class
    """
    return subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


@change_rn_dir
def reset() -> bool:
    """Function to reset changes

    Raises:
        Exception: _description_

    Returns:
        bool: _description_
    """

    common_subprocess_handler(["git", "checkout", "."])
    return True


@change_rn_dir
def remove_new_files() -> bool:
    """Function to remove new added files

    Returns:
        bool: Returns True if git command run successfully
    """

    common_subprocess_handler(["git", "clean", "-f", "-d"])

    return True
