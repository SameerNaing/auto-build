from db.models import BuildQueueModel, DriveStoreModel
from settings import GIT_CHAT_PROFILE_MAP
from common.constants import DONE, FAILED

from ..core.sendChatMessage import send_message
from ..cards import build_summary_card


__all__ = ["send_build_done_message"]


def send_build_done_message(data: BuildQueueModel, apk_share_url: str, log_share_url: str):
    """Function to send message after build process done

    Args:
        data (BuildQueueModel): builded data
        apk_share_url (str): apk file share url from google drive
        log_share_url (str): log file share url from google drive
    """
    android_error = False
    ios_error = False

    if data.build_android:
        android_error = data.android_building_status == FAILED

    if data.build_ios:
        ios_error = data.ios_building_status == FAILED

    card = build_summary_card(
        branch_name=data.branch_name,
        commit_hash=data.commit_hash,
        committer_email=data.committer_email,
        android_version_number=data.android_version_number,
        ios_version_number=data.ios_version_number,
        ios_build_number=data.ios_build_number,
        build_ios=data.build_ios == 1,
        build_android=data.build_android,
        committed_date_time=data.commit_date,
        build_started_time=data.build_started_at,
        android_error=android_error == 1,
        ios_error=ios_error,
        build_log_share_url=log_share_url,
        apk_share_url=apk_share_url
    )

    mention_user = GIT_CHAT_PROFILE_MAP.get(data.committer_email, "all")

    send_message({"text": f"<users/{mention_user}>"})
    send_message(card)
