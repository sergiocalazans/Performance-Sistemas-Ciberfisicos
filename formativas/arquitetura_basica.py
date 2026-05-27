
class ES:
  def output(self, msg):
    print(msg)

class RAM:

  def __init__(self, nbits):
    self.tam = 2**nbits
    self.ram = [0] * self.tam

  def read(self, endereco):
    return self.ram[endereco]
  
  def write(self, endereco, palavra):
    if endereco >= 0 and endereco < self.tam:
      self.ram[endereco] = palavra
    else:
      print("Endereço inválido")

  def capacidade(self):
    return self.tam

class CPU:

  def __init__(self, ram, es):
    self.es = es
    self.ram = ram
  
  def run(self, endereco):
    inicio = self.ram.read(endereco)
    fim = self.ram.read(endereco+1)

    i = 1
    for e in range(inicio, fim+1):
      self.ram.write(e, (i))
      self.es.output(f"{e} <- {i}")
      i += 1

# es1 = IO()
# es2 = IO()

# es1.output("Saída via es1")
# es2.output("Saída via es2")

es = ES()
ram = RAM(7)

# carrega o "programa" na memoria
ram.write(6, 30)
ram.write(7, 32)
cpu = CPU(ram, es)
cpu.run(6)