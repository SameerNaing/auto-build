import os
import shutil

from settings import APK_OUT_DIR, BASE_DIR

__all__ = ["move_apk_file"]


def move_apk_file(branch_name: str, apk_file_name: str) -> str:
    """Function to move apk from from RN dir to autobuild exports dir

    Args:
        branch_name (str): branch name
        apk_file_name (str): apk file name

    Returns:
        str: moved file path
    """
    move_destination = os.path.join(
        BASE_DIR, "exports", "APKs", branch_name.replace("/", "-"))
    source = os.path.join(APK_OUT_DIR, apk_file_name)

    if not os.path.exists(move_destination):
        os.makedirs(move_destination)

    move_destination = os.path.join(move_destination, apk_file_name)

    shutil.move(source, move_destination)

    return move_destination
