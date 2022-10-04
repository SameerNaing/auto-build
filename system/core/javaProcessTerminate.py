import psutil


__all__ = ["java_process_terminate"]


def java_process_terminate():
    """Function to terminate java process to release unnecessary memory allocation"""

    for process in psutil.process_iter():
        name = process.name()

        if name == "java":
            process.terminate()
