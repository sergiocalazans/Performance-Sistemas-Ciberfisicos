from multiprocessing import Semaphore, Process
from time import sleep

def down(s):
    s.acquire()

def up(s):
    s.release()

def filho(nome, n, t, depois_A, antes_D):
    if nome in ["B", "C"]:
        print(f"\t{nome} aguardando...")
        down(depois_A)

    if nome == "D":
        down(antes_D)
        down(antes_D)

    print(f"{nome} iniciando contagem (n={n}; t={t})")

    for i in range(1, n + 1):
        sleep(t)
        print(f"{nome}:{i}")

    print(f"{nome} finalizando contagem")

    if nome == "A":
        up(depois_A)
        up(depois_A)

    if nome in ["B", "C"]:
        up(antes_D)

def main():
    depois_A = Semaphore(0)
    antes_D = Semaphore(0)

    filhos = {
        "A": (5, 0.5),
        "B": (5, 1),
        "C": (5, 2),
        "D": (5, 0.25)
    }

    processos = []

    print("* GRAFO DE PRECEDÊNCIA")

    for nome, (n, t) in filhos.items():
        p = Process(target=filho, args=(nome, n, t, depois_A, antes_D))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print("FIM")

if __name__ == "__main__":
    main()
