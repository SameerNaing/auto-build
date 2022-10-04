from .credential import drive_credential


__all__ = ["share_file_link_drive"]


def share_file_link_drive(file_id: str):
    """Function to get file share url from drive

    Args:
        file_id (str): file id

    Returns:
        _type_: _description_
    """
    request_body = {"role": "reader", "type": "anyone"}

    drive_credential.permissions().create(
        fileId=file_id,
        body=request_body
    ).execute()

    data = drive_credential.files().get(
        fileId=file_id, fields="webViewLink").execute()

    return data.get("webViewLink")
