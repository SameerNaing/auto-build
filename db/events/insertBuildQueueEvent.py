from sqlalchemy.event import listens_for
from sqlalchemy.engine import Connection

from common.constants import QUEUE_CURRENT
from system.core import kill_process, delete_apk_file, delete_archive_file, delete_log_file, java_process_terminate
from google.core import send_message
from settings import GIT_CHAT_PROFILE_MAP
from git.core.actions import reset, remove_new_files

from ..utils import is_current_building, find_same_branch, merge_same_branch_data, delete_prev_queue
from ..models import BuildQueueModel


@listens_for(BuildQueueModel, "before_insert")
def insert_event(_, connection: Connection, target: BuildQueueModel):
    current = is_current_building(connection)

    if not current:
        target.queue_status = QUEUE_CURRENT
        return target

    mention = GIT_CHAT_PROFILE_MAP.get(target.committer_email, "all")
    mention = f"<users/{mention}>"
    stored_data = find_same_branch(connection, target.branch_name)
    message = {
        "text": f"{mention}, your build for {target.branch_name} is saved in queue. One build process is already running."}

    if stored_data == None:
        send_message(message)
        return target

    merge_same_branch_data(
        target=target, prev_data=stored_data)

    delete_prev_queue(connection, stored_data.id)

    if stored_data.queue_status != QUEUE_CURRENT:
        send_message(message)
        return target

    kill_process(pid=stored_data.multiprocess_pid)
    kill_process(pid=stored_data.metro_pid)
    kill_process(pid=stored_data.process_pid)
    java_process_terminate()

    delete_log_file(stored_data.branch_name, stored_data.commit_hash)
    delete_apk_file(stored_data.branch_name, stored_data.commit_hash)
    delete_archive_file(stored_data.branch_name, stored_data.commit_hash)

    reset()
    remove_new_files()

    target.queue_status = QUEUE_CURRENT

    return target
