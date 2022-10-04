import os
import shutil

from settings import RN_DIR


__all__ = ["remove_pods"]


def remove_pods():
    """Function to remove Pod folder and Pod.lock file"""

    pods_folder = os.path.join(RN_DIR, "ios", "Pods")
    pod_lock_file = os.path.join(RN_DIR, "os", "Podfile.lock")

    if os.path.exists(pods_folder):
        shutil.rmtree(pods_folder)

    if os.path.exists(pod_lock_file):
        os.unlink(pod_lock_file)
