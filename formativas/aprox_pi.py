import time

t0 = time.time()

termos = 100000000

soma = 0

num = 1

for i in range(termos):
  soma += num / (2*i+1)
  num = -num

pi = 4 * soma

d = time.time() - t0

print(f"\nPI: {pi}")
print(f"\nDesempenho: {d}s")