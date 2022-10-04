import psutil
from typing import Union

__all__ = ["kill_process"]


def kill_process(pid: Union[int, None]):
    """Function to terminate process by process id (pid)

    Args:
        pid (Union[int, None]): process id
    """
    if pid == None:
        return
    try:
        process = psutil.Process(pid=pid)
        process.terminate()
    except psutil.NoSuchProcess:
        return
    except Exception as e:
        return
