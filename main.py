from multiprocessing import Process

from trackCommit import track_commit
from build.process import process as build_process
import running

def main():
    running.show()
    p1 = Process(target=track_commit)
    p2 = Process(target=build_process)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
