from multiprocessing import Semaphore, Process, Value

def down(s):
  s.acquire()

def up(s):
  s.release()

def conta(n,vc, mutex):
    for _ in range(n):
        down(mutex)
        vc.value += 1 # região crítica
        up(mutex)

def main():
    mutex = Semaphore(1)
    vc = Value("i",0,lock=False) 

    filho1 = Process(target=conta, args=[1000000,vc,mutex])
    filho2 = Process(target=conta, args=[1000000,vc,mutex])

    filho1.start()
    filho2.start()
    
    print("aguardando filhos")
    filho1.join()
    filho2.join()
    
    print("resultado =", vc.value)

if __name__ == "__main__":
    main()
