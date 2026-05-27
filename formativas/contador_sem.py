from multiprocessing import Semaphore, Process, Value
from time import sleep

def down(s):
  s.acquire()

def up(s):
  s.release()

def filho1(n, vc, mutex, terminou_filho2, libera_filho2):
    for _ in range (1, n + 1):
        sleep(0.5)
        down(mutex)
        vc.value += 1 # região crítica
        print(f"Filho 1: {vc.value}")
        up(mutex)

    up(libera_filho2)

    down(terminou_filho2)
    print("Filho 1 chegou no ponto de encontro")

    down(mutex)
    print("Fim do filho 1")
    up(mutex)

def filho2(n, vc, mutex, terminou_filho2, libera_filho2):
    
    for i in range(1, n + 1):
       sleep(0.5)
       down(mutex)
       vc.value += 1 # região crítica
       print(f"Filho 2: {vc.value}")
       up(mutex)

       if i == (n //2):
            down(mutex)
            print("Filho 2 está aguardando o filho 1 chegar no ponto de encontro")
            up(mutex)
            down(libera_filho2)
        
    up(terminou_filho2)
    print("Filho 2 chegou no ponto de encontro")

    down(mutex)
    print("Fim do filho 2")
    up(mutex)


def main():
    mutex = Semaphore(1)
    terminou_filho2 = Semaphore(0)
    libera_filho2 = Semaphore(0)

    cont1 = Value("i",0,lock=False) 
    cont2 = Value("i",0,lock=False)

    pfilho1 = Process(target=filho1, args=[5, cont1, mutex, terminou_filho2, libera_filho2])
    pfilho2 = Process(target=filho2, args=[6, cont2, mutex, terminou_filho2, libera_filho2])

    pfilho1.start()
    pfilho2.start()
    
    print("aguardando filhos")
    pfilho1.join()
    pfilho2.join()
    
    print("resultado =", cont1.value + cont2.value)

if __name__ == "__main__":
    main()
