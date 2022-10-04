from datetime import datetime
from colorama import Fore

from git.core.info import get_yaml_data, latest_commit_info
from git.core.actions import fetch_origin
from common.utils import parse_yaml_string
from db.models import BuildQueueModel
from db.core import get_session
import db.events as _
from db.helpers import info_already_saved
from settings import RELEASE_BRANCH
from common.constants import QUEUE_PENDING


__all__ = ["build_release"]


def build_release():
    """Build the release branch"""

    fetch_origin()

    commit_hash, email, commit_datetime = latest_commit_info(
        remote_branch_name=f"origin/{RELEASE_BRANCH}")

    with get_session() as session:
        if info_already_saved(session, commit_hash):
            print(Fore.YELLOW + "Already saved in queue" + Fore.RESET)
            return

        data = get_yaml_data(
            commit_hash, remote_branch=f"origin/{RELEASE_BRANCH}")

        yaml_data = parse_yaml_string(string=data[:-2])

        session.add(BuildQueueModel(
            commit_hash=commit_hash,
            committer_email=email,
            commit_date=datetime.fromisoformat(commit_datetime),
            branch_name=RELEASE_BRANCH,
            build_android=yaml_data["build_android"],
            android_version_code=yaml_data["android_version_code"],
            android_version_number=yaml_data["android_version_number"],
            build_ios=yaml_data["build_ios"],
            ios_version_number=yaml_data["ios_version_number"],
            ios_build_number=yaml_data["ios_build_number"],
            queue_status=QUEUE_PENDING
        ))
        session.commit()
        print(Fore.GREEN + "Saved in queue." + Fore.RESET)
