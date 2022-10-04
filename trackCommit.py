import time
import schedule
from datetime import datetime

from db.core import get_session
from db.helpers import info_already_saved
import db.events as _
from db.models import BuildQueueModel
from git.core.actions import fetch_origin
from git.core.info import check_new_commit, latest_commit_info, get_yaml_data
from settings import STAGING_BRANCHES
from common.constants import QUEUE_PENDING
from common.utils import parse_yaml_string


def __task():
    with get_session() as session:
        fetch_origin()
        for branch in STAGING_BRANCHES:
            remote_branch = f"origin/{branch}"
            if not check_new_commit(branchname=branch):
                continue

            commit_hash, email, commit_datetime = latest_commit_info(
                remote_branch_name=remote_branch)

            if info_already_saved(session, commit_hash):
                continue

            data: str = get_yaml_data(commit_hash, remote_branch)

            yaml_data = parse_yaml_string(string=data[:-2])

            session.add(BuildQueueModel(
                commit_hash=commit_hash,
                committer_email=email,
                commit_date=datetime.fromisoformat(commit_datetime),
                branch_name=branch,
                build_android=yaml_data["build_android"],
                android_version_code=yaml_data["android_version_code"],
                android_version_number=yaml_data["android_version_number"],
                build_ios=yaml_data["build_ios"],
                ios_version_number=yaml_data["ios_version_number"],
                ios_build_number=yaml_data["ios_build_number"],
                queue_status=QUEUE_PENDING
            ))

            session.commit()


def track_commit():
    schedule.every(3).seconds.do(__task)
    while True:
        schedule.run_pending()
        time.sleep(1)
