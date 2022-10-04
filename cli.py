from colorama import Fore

from common.logo import LOGO, CLI_LOGO
from command.executor import execute_command


def main():
    print(Fore.MAGENTA + LOGO)
    print(CLI_LOGO + Fore.RESET)

    while True:
        command = input("##>")
        if len(command.strip()) == 0:
            continue

        execute_command(command)


if __name__ == "__main__":
    main()
