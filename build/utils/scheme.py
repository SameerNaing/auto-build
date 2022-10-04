from settings import SCHEME_BRANCH_MAP

__all__ = ["get_scheme_name"]


def get_scheme_name(branch_name: str) -> str:
    """Function to get the archive scheme name according to the given branch name

    Args:
        branch_name (str): branch name

    Returns:
        str: scheme name
    """
    return SCHEME_BRANCH_MAP.get(branch_name)
