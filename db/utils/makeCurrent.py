from sqlalchemy.engine import Connection
from sqlalchemy.sql.expression import exists

from common.constants import QUEUE_CURRENT

from ..models import BuildQueueModel


__all__ = ["make_current"]


def make_current(connection: Connection, id: int):
    """Function to change given queue id data status to "CURRENT"

    Args:
        connection (Connection): sqlalchemy connection object
        id (int): queue id
    """
    table = BuildQueueModel.__table__
    query = table.update().where(table.c.id == id).values(queue_status=QUEUE_CURRENT)
    connection.execute(query)
