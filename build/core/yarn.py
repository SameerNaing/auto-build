from sqlalchemy.orm import Session

from system.decorators import change_rn_dir
from common.process import common_subprocess_handler

from build.utils.saveRunProcess import save_run_process


__all__ = ["yarn_install", "copy_mmtools", "start_metro_server"]


@change_rn_dir
def yarn_install(session: Session, commit_hash: str):
    """Spawn "yarn install" subporcess and saves the subprocess
       process id (pid) in database.

    Args:
        session (Session): sqlalchemy orm session
        commit_hash (str): commit hash to store the pid
    """
    save_run_process(session=session, process_command=[
                     "yarn", "install"], commit_hash=commit_hash, is_metro_server=False)


@change_rn_dir
def copy_mmtools():
    """Spawn "yarn copy-mmtools"""

    common_subprocess_handler(
        ["yarn", "copy-mmtools"])


@change_rn_dir
def start_metro_server(session: Session, commit_hash: str):
    """Spawn "yarn start" subporcess and saves the subprocess
       process id (pid) in database.

    Args:
        session (Session): sqlalchemy orm session
        commit_hash (str): commit hash to store the pid
    """
    return save_run_process(session=session, process_command=[
        "yarn", "start"], commit_hash=commit_hash, is_metro_server=True)
