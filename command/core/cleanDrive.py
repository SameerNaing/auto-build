from colorama import Fore
import time

from db.helpers import get_all_drive_data
from db.core import get_session
from google.core import delete_drive_file

__all__ = ["clean_drive"]


def clean_drive():
    """Clean the drive """

    print("Deleting...")

    with get_session() as session:
        data = get_all_drive_data(session)

        for i in data:
            session.delete(i)
            session.commit()
            delete_drive_file(i.file_id)

    print(Fore.GREEN+"Successfully cleaned all drive data"+Fore.RESET)
