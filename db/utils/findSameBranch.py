from typing import Union
from sqlalchemy.engine import Connection

from ..models import BuildQueueModel

__all__ = ["find_same_branch"]


def find_same_branch(connection: Connection, branch_name: str) -> Union[None, BuildQueueModel]:
    """Function to find and return the same brach data in Queue DB if exists

    Args:
        connection (Connection): sqlalchemy connection object
        branch_name (str): branch name

    Returns:
        Union[None, BuildQueueModel]: returns queue data if the incomming commit branch has previous commit data, saved in the queue, else None
    """
    table = BuildQueueModel.__table__
    query = table.select().where(table.c.branch_name == branch_name)

    result = connection.execute(query).fetchone()

    if result == None:
        return

    return BuildQueueModel(
        id=result[0],
        commit_hash=result[1],
        committer_email=result[2],
        commit_date=result[3],
        branch_name=result[4],
        build_android=result[5],
        android_version_code=result[6],
        android_version_number=result[7],
        android_building_status=result[8],
        build_ios=result[9],
        ios_version_number=result[10],
        ios_build_number=result[11],
        ios_building_status=result[12],
        queue_status=result[13],
        multiprocess_pid=result[14],
        process_pid=result[15],
        metro_pid=result[16],
        build_started_at=result[17],
    )
