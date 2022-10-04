from db.models import BuildQueueModel
from settings import GIT_CHAT_PROFILE_MAP

from ..core import send_message
from ..cards import build_started_card

__all__ = ["send_building_message"]


def send_building_message(data: BuildQueueModel):
    """Function to send build process started info message in google chat

    Args:
        data (BuildQueueModel): build stated queue info
    """
    try:
        card = build_started_card(
            branch_name=data.branch_name,
            commit_hash=data.commit_hash,
            committer_email=data.committer_email,
            android_version_number=data.android_version_number,
            ios_version_number=data.ios_version_number,
            ios_build_number=data.ios_build_number,
            build_ios=data.build_ios == 1,
            build_android=data.build_android == 1,
            committed_date_time=data.commit_date,
            build_started_time=data.build_started_at
        )

        mention_user = GIT_CHAT_PROFILE_MAP.get(data.committer_email, "all")
        send_message({"text": f"<users/{mention_user}>"})
        send_message(card)
    except Exception as e:
        return
