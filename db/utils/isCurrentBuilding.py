from sqlalchemy.engine import Connection
from sqlalchemy.sql.expression import exists

from common.constants import QUEUE_CURRENT

from ..models import BuildQueueModel


__all__ = ["is_current_building"]


def is_current_building(connection: Connection) -> bool:
    """Funciton to check if stats "CURRENT" data exists or not

    Args:
        connection (Connection): sqlalchemy connection object

    Returns:
        bool: returns True if status "CURRENT" data exists else False
    """
    table = BuildQueueModel.__table__
    query = table.select().where(table.c.queue_status == QUEUE_CURRENT)
    query = exists(query).select()
    (current_building, ) = connection.execute(query).fetchone()

    return current_building
