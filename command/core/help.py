from tabulate import tabulate
from colorama import Fore


__all__ = ["help"]


def colored(text: str):
    return Fore.YELLOW + text + Fore.RESET


def help():
    map = {
        "show current build": "--info of the current building process",
        "show queues": "--list all the queue data",
        "delete queue <id>": "--delete queue by id",
        "clean drive": "--delete google drive files",
        "build release": "--build for release branch",
        "build first <id>": "--prioritize the given id build",
        "help":  "--show all the executable commands",
    }
    table = []
    for key, value in map.items():
        table.append([colored(key), value])
        table.append([])

    print(tabulate(table))
