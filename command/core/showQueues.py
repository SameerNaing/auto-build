from colorama import Fore, Back
from tabulate import tabulate

from common.constants import QUEUE_HOLD, QUEUE_PENDING
from db.helpers import get_all_queues, current_build_info
from db.core import get_session


__all__ = ["show_queues"]


def show_queues():
    """ Shows all the data in the queue table """

    with get_session() as session:
        queues = get_all_queues(session)

        if len(queues) == 0:
            print("The queue is empty.")
            return

    table = []

    for data in queues:

        status_color = Back.GREEN

        if data.queue_status == QUEUE_PENDING:
            status_color = Back.YELLOW

        if data.queue_status == QUEUE_HOLD:
            status_color = Back.RED

        table.append([
            f"{data.id}",
            Fore.YELLOW + f"{data.commit_hash[:7]}" + Fore.RESET,
            f"{data.committer_email}",
            Fore.GREEN + f"{data.branch_name}" + Fore.RESET,
            status_color + f" {data.queue_status} " + Back.RESET,
        ])
        table.append([])

    print(tabulate(table, headers=[
          "ID", "Commit Hash", "Committer Email", "Branch name", "Status"]))

    # message = [
    #     f"{queues.index(i) + 1}. `ID:{i.id}` | `{i.commit_hash[:7]}` | `{i.committer_email}` | `{i.branch_name}` | `{i.queue_status}`" for i in queues]
    # message = "\n\n".join(message)

    # send_message({"text": message})
