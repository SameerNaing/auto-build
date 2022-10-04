from sqlalchemy.engine import Connection

from db.models import BuildQueueModel


__all__ = ["delete_prev_queue"]


def delete_prev_queue(connection: Connection, queue_id: int):
    """Function to delete queue data by given id

    Args:
        connection (Connection): sqlalchemy connection object
        queue_id (int): queue id
    """
    table = BuildQueueModel.__table__
    query = table.delete().where(table.c.id == queue_id)
    connection.execute(query)
