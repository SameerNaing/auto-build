from sqlalchemy.orm import Session

from system.decorators import change_rn_dir, change_rn_android_dir

from ..utils.saveRunProcess import save_run_process


@change_rn_dir
def build_bundle_android(session: Session, commit_hash: str):
    """Spawn "yarn build-bundle:android" subporcess and saves the subprocess
       process id (pid) in database.

    Args:
        session (Session): sqlalchemy orm session 
        commit_hash (str): commit hash to store the pid
    """
    save_run_process(session=session, process_command=[
                     "yarn", "build-bundle:android"], commit_hash=commit_hash)


@change_rn_dir
def remove_assets(session: Session, commit_hash: str):
    """Spawn "yarn remove-assets" subporcess and saves the subprocess
       process id (pid) in database.

    Args:
        session (Session): sqlalchemy orm session 
        commit_hash (str): commit hash to store the pid
    """
    save_run_process(session=session, process_command=[
                     "yarn", "remove-assets"], commit_hash=commit_hash)


@change_rn_android_dir
def clean_project(session: Session, commit_hash: str, versionCode: str, versionNumber: str):
    """Spawn clean project subprocess

    Args:
        session (Session): sqlalchemy orm session 
        commit_hash (str): commit hash to store the pid
        versionCode (str): android version code
        versionNumber (str): android version number
    """
    save_run_process(session=session,  process_command=["./gradlew", "clean", f"-PversionCode={versionCode}", f"-PversionNumber={versionNumber}"],
                     commit_hash=commit_hash)


@change_rn_android_dir
def build_apk(session: Session, commit_hash: str, versionCode: str, versionNumber: str):
    """Spawn apk build subprocess

    Args:
        session (Session): sqlalchemy orm session 
        commit_hash (str): commit hash to store the pid
        versionCode (str): android version code
        versionNumber (str): android version number
    """
    save_run_process(session=session, process_command=[
                     "./gradlew", "assembleFmprod", f"-PversionCode={versionCode}", f"-PversionNumber={versionNumber}"], commit_hash=commit_hash)
