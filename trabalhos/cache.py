import sys


# ==========================================
# EXCEÇÃO
# ==========================================
class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender


# ==========================================
# RAM
# ==========================================
class RAM:
    def __init__(self, bits):
        self.tamanho = 2 ** bits
        self.mem = [0] * self.tamanho

    def read(self, end):
        if end < 0 or end >= self.tamanho:
            raise EnderecoInvalido(end)
        return self.mem[end]

    def write(self, end, val):
        if end < 0 or end >= self.tamanho:
            raise EnderecoInvalido(end)
        self.mem[end] = val


# ==========================================
# CACHE LINE
# ==========================================
class CacheLine:
    def __init__(self, K):
        self.tag = None
        self.dirty = False
        self.data = [0] * K


# ==========================================
# CACHE (Mapeamento Direto)
# ==========================================
class Cache:
    def __init__(self, tamanho_total, K, ram):
        self.ram = ram
        self.K = K
        self.num_linhas = tamanho_total // K
        self.linhas = [CacheLine(K) for _ in range(self.num_linhas)]

        self.bits_w = 6
        self.bits_r = 6
        self.bits_t = 22 - self.bits_w - self.bits_r

    def separar(self, end):
        w = end & ((1 << self.bits_w) - 1)
        r = (end >> self.bits_w) & ((1 << self.bits_r) - 1)
        t = end >> (self.bits_w + self.bits_r)
        return t, r, w

    def read(self, end):
        t, r, w = self.separar(end)
        linha = self.linhas[r]

        # HIT
        if linha.tag == t:
            return linha.data[w]

        # MISS
        self.miss(end, t, r)
        return self.linhas[r].data[w]

    def write(self, end, val):
        t, r, w = self.separar(end)
        linha = self.linhas[r]

        if linha.tag != t:
            self.miss(end, t, r)

        linha.data[w] = val
        linha.dirty = True

    def miss(self, end, t, r):
        linha = self.linhas[r]

        bloco_inicio = (end // self.K) * self.K
        bloco_fim = bloco_inicio + self.K - 1

        # Caso haja substituição
        if linha.tag is not None:
            antigo_inicio = ((linha.tag << self.bits_r) | r) << self.bits_w
            antigo_fim = antigo_inicio + self.K - 1

            print(f"MISS: {end} L{r}->[{antigo_inicio}..{antigo_fim}] | "
                  f"[{bloco_inicio}..{bloco_fim}]->L{r}")
        else:
            print(f"MISS: {end} [{bloco_inicio}..{bloco_fim}]->L{r}")

        # Carrega bloco da RAM
        for i in range(self.K):
            linha.data[i] = self.ram.read(bloco_inicio + i)

        linha.tag = t
        linha.dirty = False


# ==========================================
# IO
# ==========================================
class IO:
    def output(self, end, valor):
        print(f"   > {end} = {valor}")


# ==========================================
# CPU
# ==========================================
class CPU:
    def __init__(self, cache, io):
        self.cache = cache
        self.io = io

    def run(self, inicio):
        valor = 1
        for i in range(13):
            end = inicio + i
            self.cache.read(end)
            self.io.output(end, valor)
            valor += 1


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================
try:
    io = IO()
    ram = RAM(22)  # 4M
    cache = Cache(4 * 2**10, 64, ram)
    cpu = CPU(cache, io)

    inicio = 0

    print("Programa 1")
    cpu.run(inicio)

    print("\nPrograma 2")
    cache.write(inicio, 4155)
    cache.write(inicio + 1, 4165)
    cpu.run(inicio)

except EnderecoInvalido as e:
    print("Endereco inválido:", e.ender, file=sys.stderr)
