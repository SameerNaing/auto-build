from datetime import datetime

from common.utils import format_message_date

__all__ = ["build_summary_card"]


def build_summary_card(branch_name: str, commit_hash: str, committer_email: str,
                       android_version_number: str, ios_version_number: str, ios_build_number: int,
                       build_ios: bool, build_android: bool, committed_date_time: datetime,
                       build_started_time: datetime, android_error: bool, ios_error: bool,
                       build_log_share_url: str, apk_share_url: str):

    dynamic_data = []

    if build_android:
        dynamic_data.append({"keyValue": {
            "topLabel": "Android Version Number",
            "content": android_version_number
        }})

    if build_android and not android_error and apk_share_url != None:
        dynamic_data.append({"keyValue": {
            "topLabel": "Apk Download Url",
            "content": apk_share_url
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

    subtitle = "Successful"

    if android_error or ios_error:
        subtitle = f"{'Android Failed' if android_error else'' } {'|' if android_error and ios_error else ''} {'IOS Failed' if ios_error else ''}"

    return {
        "cards": [
            {
                "header": {
                    "title": "Build Summary",
                    "subtitle": subtitle
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
                                    "topLabel": "Commit",
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
                                    "topLabel": "Builded",
                                    "content": f"{'Android' if build_android else ''}{' | ' if build_android and build_ios else ''}{'IOS' if build_ios else ''}"
                                }
                            },
                            {
                                "keyValue": {
                                    "topLabel": "Build Process Started Time",
                                    "content": format_message_date(build_started_time)
                                }
                            },
                            * dynamic_data,
                            {
                                "keyValue": {
                                    "topLabel": "Complete Build Log",
                                    "content": build_log_share_url or "_"
                                }
                            }
                        ]
                    },
                ]
            }
        ]
    }
