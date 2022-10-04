from colorama import Fore

from db.helpers import get_queue_by_id, delete_by_id
from db.core import get_session
from system.core import kill_process, delete_archive_file, delete_apk_file, delete_log_file, java_process_terminate
from git.core.actions import reset, remove_new_files
from common.constants import QUEUE_CURRENT

__all__ = ["delete_queue"]


def delete_queue(id: int):
    """Delete the queue data"""

    with get_session() as session:
        data = get_queue_by_id(session, id)

        if data == None:
            print(Fore.YELLOW + f"ID:{id}" + Fore.RESET, "does not exists.")
            return

        if data.queue_status == QUEUE_CURRENT:
            reset()
            remove_new_files()

            kill_process(data.multiprocess_pid)
            kill_process(data.process_pid)
            kill_process(data.metro_pid)
            java_process_terminate()

            delete_log_file(data.branch_name, data.commit_hash)
            delete_apk_file(data.branch_name, data.commit_hash)
            delete_archive_file(data.branch_name, data.commit_hash)

        delete_by_id(session, id)

        print(Fore.GREEN + "Queue Deleted Successfully" + Fore.RESET)
