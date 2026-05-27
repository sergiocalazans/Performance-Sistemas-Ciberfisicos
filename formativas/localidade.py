from time import time

t0 = time()

def soma(m):
  res = 0
  for i in range(len(m)):
    for j in range(len(m[0])):
      res += m[i][j]

  return res

matriz =[[1] * 16000 for _ in range(16000)]

print(soma(matriz))
print("duração: ", time() - t0)
