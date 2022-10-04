from colorama import Fore

from db.core import get_session
from db.helpers import get_queue_by_id, current_build_info
from system.core import kill_process, java_process_terminate
from git.core.actions import reset, remove_new_files
from common.constants import QUEUE_CURRENT, QUEUE_HOLD


__all__ = ["build_first"]


def build_first(id: int):
    """Prioritize the build of the given id

    Args:
        id (int): ID of the queue to build first
    """
    with get_session() as session:
        data = get_queue_by_id(session, id)
        current = current_build_info(session)

        if data == None:
            print(Fore.YELLOW + f"ID:{id}", Fore.RESET + "does not exists")
            return

        # If all the data are hold and no current build then
        if current == None:
            reset()
            remove_new_files()
            data.queue_status = QUEUE_CURRENT
            session.commit()
            return

        if current.id == data.id:
            print("Build process is already running for this",
                  Fore.YELLOW + f"ID:{id} " + Fore.RESET)
            return

        data.queue_status = QUEUE_CURRENT
        current.queue_status = QUEUE_HOLD
        session.commit()

        reset()
        remove_new_files()

        kill_process(current.multiprocess_pid)
        kill_process(current.metro_pid)
        kill_process(current.process_pid)
        java_process_terminate()
