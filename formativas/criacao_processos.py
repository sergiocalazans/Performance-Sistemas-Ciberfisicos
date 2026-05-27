from time import time, sleep
from os import getpid, getppid
from multiprocessing import Process

def cont(N: int, T: float) -> None:

  print(f"PID: {getpid()}")
  print(f"PPID: {getppid()}")

  for i in range(N):
    print(i + 1)
    sleep(T)


if __name__ == "__main__":

    t0 = time()
    p1 = Process(target=cont, args=(10, 1))
    p1.start()
    print("Fim do pai")

    p2 = Process(target=cont, args=(30, 0.5))
    p2.start()
    p2.join()
    print("Fim do pai")
    print(f"Tempo de execução: {time() - t0} segundos")
