from settings import ARCHIVE_NAME_BRANCH_MAP


__all__ = ["get_archive_name"]


def get_archive_name(branch_name: str) -> str:
    """Function to get archive file name according to the branch

    Args:
        branch_name (str): the branch name

    Returns:
        str: Returns archive file name according to the branch
    """
    return ARCHIVE_NAME_BRANCH_MAP.get(branch_name)
