from sqlalchemy.event import listens_for
from sqlalchemy.engine import Connection

from system.core import java_process_terminate

from ..utils import get_pending_data, make_current, get_hold_data
from ..models import BuildQueueModel


@listens_for(BuildQueueModel, "after_delete")
def delete_event(_, connection: Connection, target: BuildQueueModel):
    java_process_terminate()

    id = get_hold_data(connection)

    if id != None:
        make_current(connection, id)
        return

    id = get_pending_data(connection)

    if id != None:
        make_current(connection, id)
