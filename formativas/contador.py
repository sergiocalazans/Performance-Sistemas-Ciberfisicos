from time import time, sleep
from os import getpid, getppid

def cont(N: int, T: float) -> None:
    for i in range(N):
        print(i + 1)
        sleep(T)

if __name__ == "__main__":
    print(f"PID: {getpid()}, PPID: {getppid()}")
    cont(12, 0.5)