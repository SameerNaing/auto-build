from common.utils import utf_8_to_string
from system.decorators import change_rn_dir
from common.process import common_subprocess_handler


@change_rn_dir
def check_new_commit(branchname: str) -> bool:
    """Function to check if there is new commit on remote branch

    Args:
        remote_branch_name (str): remote branch name

    Raises:
        Exception: error on git command

    Returns:
        bool: Returns True if there is an new commit on remote
    """

    out = common_subprocess_handler(
        ["git", "diff", branchname, f"origin/{branchname}"])

    if len(out.decode("utf-8")):
        return True

    return False


@change_rn_dir
def latest_commit_info(remote_branch_name: str) -> tuple[str, str, str, str]:
    """Function to get lastest commit info on remote branch

    Args:
        remote_branch_name (str): remote branch name

    Raises:
        Exception: if git command get error

    Returns:
        full_hash: Full hash code of commit
        abb_hash: Abbreviated hash code of commit
        email: Committer email
        commit_datetime: committed datetime in ISO format
    """

    out = common_subprocess_handler(
        ["git", "show", remote_branch_name, "--pretty='%H|%ce|%cI'", "--no-patch"])

    out = out.decode("utf-8")
    out = "".join(utf_8_to_string(out)).split("|")

    commit_hash, email, commit_datetime = out

    return commit_hash, email, commit_datetime


@change_rn_dir
def current_working_branch() -> str:
    """Funtion to get the name of the current working branch

    Raises:
        Exception: error on command

    Returns:
        str: Name of the current branch
    """
    out = common_subprocess_handler(["git", "branch", "--show-current"])

    out = out.decode("utf-8")

    return utf_8_to_string(out)


@change_rn_dir
def get_yaml_data(commit_hash: str, remote_branch: str) -> str:
    """Function to get build.yaml data from origin of given commit hash

    Args:
        commit_hash (str): commit hash
        remote_branch (str): remote branch name

    Returns:
        str: build.yaml file content
    """
    out = common_subprocess_handler(
        ["git", "show", f"{remote_branch}:build.yaml",
         commit_hash, "--pretty=format:''", "--no-patch"])
    out = out.decode("utf-8")
    return out
