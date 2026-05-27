from multiprocessing import Semaphore, Process
from time import sleep

aOK = Semaphore(0) 

def down(s):
  s.acquire()

def up(s):
  s.release()

def a():
  sleep(5)
  print("a OK")

def b():
  print("b OK")

def A(aOK):
  up(aOK)
  a()

def B(aOK):
  down(aOK)
  b()


if __name__ == "__main__":
  pA = Process(target=A, args=[aOK])
  pB = Process(target=B, args=[aOK])

  pA.start()
  pB.start()

  pA.join()
  pB.join()