from sqlalchemy.engine import Connection

from db.models import BuildQueueModel
from common.constants import UPLOADING, BUILDING, DONE


__all__ = ["merge_same_branch_data"]


def merge_same_branch_data(target: BuildQueueModel, prev_data: BuildQueueModel) -> BuildQueueModel:
    """Function to merge same brach commit info

    Args:
        target (BuildQueueModel): incomming insert target data
        prev_data (BuildQueueModel): already stored data

    Returns:
        BuildQueueModel: merged data
    """
    target.build_android = target.build_android or prev_data.build_android
    target.build_ios = target.build_ios or prev_data.build_ios
    target.ios_build_number = target.ios_build_number + \
        1 if prev_data.ios_building_status == DONE and target.ios_build_number == prev_data.ios_build_number else target.ios_build_number
