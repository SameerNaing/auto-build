import time
from multiprocessing import Process

from db.core import get_session
from db.models import BuildQueueModel
from common.constants import QUEUE_CURRENT

from .builder import builder


def __task():
    with get_session() as session:
        current: BuildQueueModel = session.query(BuildQueueModel).filter(
            BuildQueueModel.queue_status == QUEUE_CURRENT).first()

        if current == None:
            return
        process = Process(target=builder, kwargs={"queue_id": current.id})
        process.start()
        process.join()


def process():
    while True:
        __task()
        time.sleep(1)
