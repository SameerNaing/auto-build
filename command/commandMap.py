from .core import build_first, build_release, clean_drive, delete_queue, show_current_building, show_queues, help

mapper = {
    "show current build": show_current_building,
    "show queues": show_queues,
    "delete queue": delete_queue,
    "clean drive": clean_drive,
    "build release": build_release,
    "build first": build_first,
    "help":  help,
}
