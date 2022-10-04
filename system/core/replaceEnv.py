from system.decorators import change_rn_dir
from settings import ENV_BRANCH_MAP


__all__ = ["replace_env"]


@change_rn_dir
def replace_env(branch_name: str) -> str:
    """Function to replace .env file content according to app flavour

    Args:
        branch_name (str): branch name

    Returns:
        str: replaced env file name
    """
    replace_with = ENV_BRANCH_MAP.get(branch_name, ".env.fmprod")
    with open(replace_with, "r") as reference_env, open(".env", "r+") as env:
        env.truncate(0)
        for line in reference_env:
            env.write(line)
    return replace_with
