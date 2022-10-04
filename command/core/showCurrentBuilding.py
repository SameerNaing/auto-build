from tabulate import tabulate
from colorama import Fore, Back

from common.utils import format_message_date
from db.core import get_session
from db.helpers import current_build_info


__all__ = ["show_current_building"]


def show_current_building():
    """Show detail of the current building process"""

    with get_session() as session:
        current = current_build_info(session)

    if current == None:
        print("No build process is running.")
        return

    android = f"{current.android_building_status or 'Not Started'}"
    ios = f"{current.ios_building_status}" or "Not Started"

    table = []

    table.append([
        "Commit hash",
        Fore.YELLOW + f"{current.commit_hash}" + Fore.RESET
    ])

    table.append([])

    table.append([
        "Committer email",
        f"{current.committer_email}"
    ])

    table.append([])

    table.append([
        "Branch name",
        Fore.GREEN + f"{current.branch_name}" + Fore.RESET
    ])

    table.append([])

    if current.build_started_at != None:
        table.append([
            "Build Started At",
            Fore.MAGENTA +
            f"{format_message_date(current.build_started_at)}" + Fore.RESET
        ])

        table.append([])

    if current.build_ios == 1:
        table.append([
            "IOS version number",
            current.ios_version_number
        ])

        table.append([])

        table.append([
            "IOS build number",
            current.ios_build_number
        ])
        table.append([])
        table.append(["IOS Status", ios])
        table.append([])

    if current.build_android == 1:
        table.append(
            ["Android Version", f"{current.android_version_code}({current.android_version_number})"])
        table.append([])
        table.append(["Android Status", android])
        table.append([])

    table.append([
        "Status",
        Back.GREEN + f" {current.queue_status} " + Back.RESET
    ])

    print(tabulate(table))
