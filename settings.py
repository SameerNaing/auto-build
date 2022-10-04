import os

# Directories
BASE_DIR = os.path.dirname(__file__)
RN_DIR = "Your mobile app dir"
APK_OUT_DIR = os.path.join(RN_DIR, "android", "app", "build",
                           "outputs", "apk", "fmprod", "release")


# Git Branch Settings
STAGING_BRANCHES = ["List all the staging branched"]
RELEASE_BRANCH = "master branch"

# Map the branch with .env file
ENV_BRANCH_MAP = {
    "branch name":".env file name"
}


# IOS Archive Settings

# Map the branch with IOS Scheme name
SCHEME_BRANCH_MAP = {
    "branch name": "Scheme name"
}

# Map the branch with the .xcarchive file name
ARCHIVE_NAME_BRANCH_MAP = {
   "branch name":".xcarchive file name"
}

# Google Chat Settings

# Map the developer's google chat id with the github email 
GIT_CHAT_PROFILE_MAP = {
    "github email": "chat user id"
}

CHAT_SPACE_ID = "Bot chat space name"


# Google Drive Settings

# Map the log folder upload google drive parent folder id with branch name
LOGS_FOLDER_BRANCH_MAP = {
   "branch name":"drive parent folder id"
}

# Map the APK upload googl drive parent folder id with branch name
APK_FOLDER_BRANCH_MAP = {
    "branch name":"drive parent folder id"

}
