from colorama import Fore

__all__ = ["no_command"]


def no_command():
    """No command exists message"""

    print("No command exists.", "Please type", Fore.YELLOW+"help" +
          Fore.RESET, "to see available execuatable commands.")
