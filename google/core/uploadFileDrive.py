from googleapiclient.http import MediaFileUpload

from .credential import drive_credential


__all__ = ["upload_file_drive"]


def upload_file_drive(parent_folder: str, meta_file_name: str, mimetype: str, upload_file_path: str) -> str:
    """Function to upload local file to drive

    Args:
        parent_folder (str): google drive parent folder id for saving the upload file
        meta_file_name (str): upload file meta data
        mimetype (str): file mime type
        upload_file_path (str): upload file location

    Returns:
        str: uploaded file id from api response
    """
    file_meta = {"name": meta_file_name, "parents": [parent_folder]}
    media = MediaFileUpload(upload_file_path, mimetype)

    data = drive_credential.files().create(body=file_meta, media_body=media,
                                           fields="id", supportsAllDrives=True).execute()

    return data.get("id")
