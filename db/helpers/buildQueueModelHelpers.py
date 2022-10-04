from sqlalchemy.orm import Session
from typing import Union, List

from common.constants import QUEUE_CURRENT

from ..models import BuildQueueModel


__all__ = ["info_already_saved", "current_build_info",
           "get_all_queues", "get_queue_by_id", "delete_by_id", "set_metro_pid", "set_process_id"]


def info_already_saved(session: Session, commit_hash: str) -> bool:
    """Function to check if the commit data is already saved in DB or not

    Args:
        session (Session): sqlalchemy session
        commit_hash (str): commit hash

    Returns:
        bool: returns True if the data already exists in DB else False
    """
    exists = session.query(BuildQueueModel).filter(
        BuildQueueModel.commit_hash == commit_hash).exists()
    exists = session.query(exists).scalar()
    return exists


def current_build_info(session: Session) -> Union[None, BuildQueueModel]:
    """Function to get currently building process info

    Args:
        session (Session): sqlalchemy session

    Returns:
        Union[None, BuildQueueModel]: returns None if no current build process running else returns the data
    """
    data = session.query(BuildQueueModel).filter(
        BuildQueueModel.queue_status == QUEUE_CURRENT).first()
    return data


def get_all_queues(session: Session) -> List[BuildQueueModel]:
    """Function to get all the data inside BuildQueue Table

    Args:
        session (Session): sqlalchemy session

    Returns:
        Union[None, List[BuildQueueModel]]: returns None if the table is empty else returns List of data
    """
    data = session.query(BuildQueueModel).all()
    return data


def get_queue_by_id(session: Session, id: int) -> Union[None, BuildQueueModel]:
    """Function to get queue data by queue id

    Args:
        session (Session): sqlalchemy session
        id (int): queue id 

    Returns:
        Union[None, BuildQueueModel]: returns data if exists else None
    """
    data = session.query(BuildQueueModel).get(id)
    return data


def delete_by_id(session: Session, id: int):
    """Function to delete queue data by id

    Args:
        session (Session): sqlalchemy session
        id (int): queue id
    """
    data = session.query(BuildQueueModel).get(id)
    session.delete(data)
    session.commit()


def set_metro_pid(session: Session, commit_hash: str, pid: int):
    """Function to save metro server process id to DB

    Args:
        session (Session): sqlalchemy session
        commit_hash (str): commit hash
        pid (int): process id
    """
    data = session.query(BuildQueueModel).filter(
        BuildQueueModel.commit_hash == commit_hash).first()

    data.metro_pid = pid
    session.commit()


def set_process_id(session: Session, commit_hash: str, pid: int):
    """Function to save running process id eg. "pod install", "yarn install" etc

    Args:
        session (Session): sqlalchemy session
        commit_hash (str): commit hash
        pid (int): process id
    """
    data = session.query(BuildQueueModel).filter(
        BuildQueueModel.commit_hash == commit_hash).first()

    data.process_pid = pid
    session.commit()
