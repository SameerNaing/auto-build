import os

from settings import RN_DIR


__all__ = ["change_rn_android_dir"]


def change_rn_android_dir(func):
    def wrapper(*args, **kwargs):
        os.chdir(os.path.join(RN_DIR, "android"))
        return func(*args, **kwargs)
    return wrapper
