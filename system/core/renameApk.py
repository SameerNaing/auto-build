import os

from settings import APK_OUT_DIR
from system.decorators import change_rn_android_dir


__all__ = ["rename_generated_apk"]


@change_rn_android_dir
def rename_generated_apk(commit_hash):
    for file in os.listdir(APK_OUT_DIR):
        if file.endswith(".apk"):
            old_name = os.path.join(APK_OUT_DIR, file)
            new_name = os.path.join(APK_OUT_DIR, f"{commit_hash}.apk")
            os.rename(old_name, new_name)

    return f"{commit_hash}.apk"
