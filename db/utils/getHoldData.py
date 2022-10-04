from sqlalchemy.engine import Connection
from typing import Union

from db.models import BuildQueueModel
from common.constants import QUEUE_HOLD


__all__ = ["get_hold_data"]


def get_hold_data(connection: Connection) -> Union[int, None]:
    """Function to get status "HOLD" data from queue table

    Args:
        connection (Connection): sqlalchemy connection object

    Returns:
        Union[int, None]: returns the id of the hold queue data if exists, else None
    """
    table = BuildQueueModel.__table__
    query = table.select().where(table.c.queue_status == QUEUE_HOLD)

    data = connection.execute(query).fetchone()

    if data == None:
        return None

    id, *_ = data
    return id
