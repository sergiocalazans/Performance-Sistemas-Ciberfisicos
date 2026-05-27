import time

t0 = time.time()

for _ in range(5000000):
  print("X", end="")

d = time.time() - t0

print(f"\nTempo: {d}s")
