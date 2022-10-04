from typing import Union
from sqlalchemy.engine import Connection
from sqlalchemy import asc

from common.constants import QUEUE_PENDING

from ..models import BuildQueueModel


__all__ = ["get_pending_data"]


def get_pending_data(connection: Connection) -> Union[int, None]:
    """Function to get status "PENDING" data from queue

    Args:
        connection (Connection): sqlalchemy connection object

    Returns:
        Union[int, None]: return id of the pending data if exists else None
    """
    table = BuildQueueModel.__table__
    query = table.select().where(table.c.queue_status ==
                                 QUEUE_PENDING).order_by(asc(table.c.commit_date))
    data = connection.execute(query).fetchone()

    if data == None:
        return None

    id, *_ = data

    return id
