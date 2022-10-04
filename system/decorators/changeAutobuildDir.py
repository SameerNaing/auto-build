import os

from settings import BASE_DIR


__all__ = ["change_autobuild_dir"]


def change_autobuild_dir(func):
    def wrapper(*args, **kwargs):
        os.chdir(BASE_DIR)
        return func(*args, **kwargs)
    return wrapper
