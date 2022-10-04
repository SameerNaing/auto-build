from datetime import datetime
from common.constants import DONE, FAILED

from common.utils import format_message_date


__all__ = ["build_started_card"]


def build_started_card(branch_name: str, commit_hash: str, committer_email: str,
                       android_version_number: str, ios_version_number: str, ios_build_number: int,
                       build_ios: bool, build_android: bool, committed_date_time: datetime,
                       build_started_time: datetime):

    dynamic_data = []

    if build_android:
        dynamic_data.append({"keyValue": {
            "topLabel": "Android Version Number",
            "content": android_version_number
        }})

    if build_ios:
        dynamic_data.append({"keyValue": {
            "topLabel": "IOS Version Number",
            "content": ios_version_number
        }})

        dynamic_data.append({"keyValue": {
            "topLabel": "IOS Build Number",
            "content": str(ios_build_number)
        }})

    return {
        "cards": [
            {
                "header": {
                    "title": "Start Buiding",
                    "subtitle": "Build process is started for your commit."
                },
                "sections": [
                    {
                        "widgets": [
                            {
                                "keyValue": {
                                    "topLabel": "Branch Name",
                                    "content": branch_name
                                }
                            },
                            {
                                "keyValue": {
                                    "topLabel": "Commit Hash",
                                    "content": commit_hash
                                }
                            },
                            {
                                "keyValue": {
                                    "topLabel": "Committer",
                                    "content": committer_email
                                }
                            },
                            {
                                "keyValue": {
                                    "topLabel": "Committed Time",
                                    "content": format_message_date(committed_date_time)
                                }
                            },

                            {
                                "keyValue": {
                                    "topLabel": "Building For",
                                    "content": f"{'Android' if build_android else ''}{' | ' if build_android and build_ios else ''}{'IOS' if build_ios else ''}"
                                }
                            },
                            *dynamic_data,
                            {
                                "keyValue": {
                                    "topLabel": "Build Process Started Time",
                                    "content": format_message_date(build_started_time)
                                }
                            },

                        ]
                    },
                ]
            }
        ]
    }
