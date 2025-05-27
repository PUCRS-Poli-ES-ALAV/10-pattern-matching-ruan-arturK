import random
import string
import time

def pattern_match(s1, s2):
    n = len(s1)
    m = len(s2)
    iteracoes = 0
    instrucoes = 0

    for i in range(n - m + 1):
        iteracoes += 1  # Conta cada iteração do laço externo
        match = True
        for j in range(m):
            instrucoes += 1  # Conta cada comparação
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return i, iteracoes, instrucoes
    return -1, iteracoes, instrucoes

# Gerar strings grandes
tamanho_s1 = 600_000
tamanho_s2 = 500

# Gera s1 aleatória
s1 = ''.join(random.choices(string.ascii_uppercase, k=tamanho_s1))
# Gera s2 aleatória
s2 = ''.join(random.choices(string.ascii_uppercase, k=tamanho_s2))

# Opcional: para garantir que s2 aparece em s1, insira s2 em uma posição aleatória de s1
pos_insercao = random.randint(0, tamanho_s1 - tamanho_s2)
s1 = s1[:pos_insercao] + s2 + s1[pos_insercao + tamanho_s2:]

# Medir tempo de execução
inicio = time.time()
pos, it, inst = pattern_match(s1, s2)
fim = time.time()

print(f"Posição encontrada: {pos}")
print(f"Iterações: {it}")
print(f"Instruções: {inst}")
print(f"Tempo de execução: {fim - inicio:.2f} segundos")