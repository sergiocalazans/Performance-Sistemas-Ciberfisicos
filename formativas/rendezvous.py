from multiprocessing import Semaphore, Process
from time import sleep

a1OK = Semaphore(0)
b1OK = Semaphore(0)

def down(s):
  s.acquire()

def up(s):
  s.release()

def a1():
  sleep(5)
  print("a1 ok")

def a2():
  print("a2 ok")

def A(a1OK):
  a1()
  up(a1OK)
  down(b1OK)
  a2()

def b1():
  sleep(2)
  print("b1 ok")

def b2():
  print("b2 ok")

def B(b1OK):
  b1()
  up(b1OK)
  down(a1OK)
  b2()

if __name__ == "__main__":
  pA = Process(target=A, args=[a1OK])
  pB = Process(target=B, args=[b1OK])

  pA.start()
  pB.start()

  pA.join()
  pB.join()