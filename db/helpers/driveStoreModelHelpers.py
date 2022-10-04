from typing import List, Union
from sqlalchemy.orm import Session

from common.constants import DRIVE_APK_FILE, DRIVE_LOG_FILE

from ..models import DriveStoreModel


__all__ = ["save_drive_info", "get_drive_data",
           "get_drive_share_url", "get_all_drive_data"]


def save_drive_info(session: Session, file_id: str, commit_hash: str, share_url: str, file_type: Union[DRIVE_APK_FILE, DRIVE_LOG_FILE]):
    """Function to save drive data

    Args:
        session (Session): sqlalchemy session
        file_id (str): file id from google drive api
        commit_hash (str): commit hash
        share_url (str): google drive file share url
        file_type (Union[DRIVE_APK_FILE, DRIVE_LOG_FILE]): file type "APK" or "LOG"
    """
    session.add(DriveStoreModel(file_id=file_id, commit_hash=commit_hash,
                                share_url=share_url, file_type=file_type))
    session.commit()


def get_drive_data(session: Session, commit_hash: str, fileType: Union[DRIVE_APK_FILE, DRIVE_LOG_FILE]) -> Union[None, str]:
    """Function to get drive data by commit hash

    Args:
        session (Session): sqlalchemy session
        commit_hash (str): commit hash
        fileType (Union[DRIVE_APK_FILE, DRIVE_LOG_FILE]): file type "APK" or "LOG"

    Returns:
        Union[None, str]: returns shared url if not None
    """
    return session.query(DriveStoreModel).filter(DriveStoreModel.commit_hash == commit_hash, DriveStoreModel.file_type == fileType).first()


def get_drive_share_url(session: Session, commit_hash, fileType: Union[DRIVE_APK_FILE, DRIVE_LOG_FILE]) -> Union[str, None]:
    data: DriveStoreModel = session.query(DriveStoreModel).filter(DriveStoreModel.commit_hash ==
                                                                  commit_hash, DriveStoreModel.file_type == fileType).first()

    if data == None:
        return

    return data.share_url


def get_all_drive_data(session: Session) -> List[DriveStoreModel]:
    """Function to get all the drive stored data

    Args:
        session (Session): sqlalchemy session

    Returns:
        List[DriveStoreModel]: data from DriveStore table
    """
    return session.query(DriveStoreModel).all()
