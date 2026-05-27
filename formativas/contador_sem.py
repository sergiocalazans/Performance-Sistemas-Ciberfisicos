from multiprocessing import Semaphore, Process, Value
from time import sleep

def down(s):
  s.acquire()

def up(s):
  s.release()

def contP1(n, vc, sem, terminou_contP2, libera_contP2):
    for _ in range (1, n + 1):
        sleep(0.5)
        down(sem)
        vc.value += 1 # região crítica
        print(f"Filho 1: {vc.value}")
        up(sem)

    up(libera_contP2)

    down(terminou_contP2)
    print("Filho 1 chegou no ponto de encontro")

    down(sem)
    print("Fim do filho 1")
    up(sem)

def contP2(n, vc, sem, terminou_contP2, libera_contP2):
    
    for i in range(1, n + 1):
       sleep(0.5)
       down(sem)
       vc.value += 1 # região crítica
       print(f"Filho 2: {vc.value}")
       up(sem)

       if i == (n // 2):
            down(sem)
            print("Filho 2 está aguardando o filho 1 chegar no ponto de encontro")
            up(sem)
            down(libera_contP2)
        
    up(terminou_contP2)
    print("Filho 2 chegou no ponto de encontro")

    down(sem)
    print("Fim do filho 2")
    up(sem)


def main():
    sem = Semaphore(1)
    terminou_contP2 = Semaphore(0)
    libera_contP2 = Semaphore(0)

    cont1 = Value("i",0,lock=False) 
    cont2 = Value("i",0,lock=False)

    pfilho1 = Process(target=contP1, args=[5, cont1, sem, terminou_contP2, libera_contP2])
    pfilho2 = Process(target=contP2, args=[6, cont2, sem, terminou_contP2, libera_contP2])

    pfilho1.start()
    pfilho2.start()
    
    print("aguardando filhos")
    
    pfilho1.join()
    pfilho2.join()
    
    print("resultado =", cont1.value + cont2.value)

if __name__ == "__main__":
    main()
