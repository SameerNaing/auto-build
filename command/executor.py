from .commandMap import mapper
from .core import no_command


def execute_command(command: str):
    """Function to map command string to command execute function

    Args:
        command (str): input command
        mention_sender (str): mention sender id to notify
    """
    command = command.lower()

    if "delete queue" in command or "build first" in command:
        command = command.split(" ")
        command, id = " ".join(command[:2]), command[-1]
        mapper[command](id=id)
        return

    if command not in mapper:
        no_command()
        return

    mapper[command]()
