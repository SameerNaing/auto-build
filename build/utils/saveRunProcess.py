from typing import Union, List
import subprocess
from sqlalchemy.orm import Session

from db.helpers import set_metro_pid, set_process_id


__all__ = ["save_run_process"]


def save_run_process(session: Session, process_command: List[str], commit_hash: str, is_metro_server: bool = False) -> Union[subprocess.Popen, None]:
    """Function to spawn the subprocess and saves the pid to the database.

    Args:
        session (Session): sqlalchemy orm session
        process_command (List[str]): subprocess command in list.
        commit_hash (str): commit hash to store the pid
        is_metro_server (bool): if is metro server, it won't communicate with the process, only run in the background.

    Raises:
        Exception: if the subprocess return code is not 0.

    Returns:
        subprocess.Popen | None : Returns subprocess.Popen class, if is_metro_server is True else returns nothing
    """

    process = subprocess.Popen(
        process_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    if (is_metro_server):
        set_metro_pid(session, commit_hash, process.pid)
        return process

    set_process_id(session, commit_hash, process.pid)

    _, err = process.communicate()

    if process.returncode != 0:
        raise Exception(err.decode("utf-8"))
