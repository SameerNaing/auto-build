import os

from settings import RN_DIR


__all__ = ["change_rn_dir"]


def change_rn_dir(func):
    def wrapper(*args, **kwargs):
        os.chdir(RN_DIR)
        return func(*args, **kwargs)
    return wrapper
