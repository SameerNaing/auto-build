from system.decorators import change_rn_ios_dir


__all__ = ["change_archive_config"]


@change_rn_ios_dir
def change_archive_config(version_number: str, build_number: int):
    """Function to change ios archive config file contents

    Args:
        version_number (str): verions number
        build_number (int): build number
    """
    with open("archiveConfig.xcconfig", "r+") as f:
        f.truncate(0)
        f.write(f"MARKETING_VERSION={version_number}")
        f.write("\n")
        f.write(f"CURRENT_PROJECT_VERSION={build_number}")
