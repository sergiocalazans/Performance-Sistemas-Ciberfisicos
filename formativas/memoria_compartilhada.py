from multiprocessing import Process, Value
from threading import Thread
from time import time

valor = 1000000
ct = Value('i', 0, lock=False)
qtd_threads = 2
processos = ['A', 'B']
threads = []
vez = 'A'

def contar(N, C, P) -> None:

  while vez != P: pass
  vez = processos.index(P) + 1
  for _ in range(N):
    C.value += 1
  vez = processos.index(P) - 1
    
def criar_threads(N: int) -> None:
    for i in range(N):
        t = Thread(target=contar, args=[valor, ct, processos[i]])
        t.start()
        threads.append(t)

def encerra_threads() -> None:
    for t in threads:
        t.join()

def testar_threads() -> None:
    print("\nTestando Threads")
    t0 = time()
    criar_threads(qtd_threads)
    encerra_threads()
    print(f"\nThreads - Contador final: {ct.value}")
    t1 = time()
    print(f"Tempo total: {t1 - t0}")

if __name__ == "__main__":
    testar_threads()