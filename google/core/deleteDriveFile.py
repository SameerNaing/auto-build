from .credential import drive_credential

__all__ = ["delete_drive_file"]


def delete_drive_file(file_id: str):
    """Function to delete drive file 

    Args:
        file_id (str): file id from google drive api
    """
    try:
        drive_credential.files().delete(fileId=file_id).execute()
    except Exception as e:
        return
