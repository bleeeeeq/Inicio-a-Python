# Exercício número 20

# Ativando a função e guardando os números

def is_prime(Num):
    if Num < 2:
        return False
    for i in range(2, int(Num ** 0.5) + 1):
        if Num % i == 0:
            return False
    return True

NumTotal = []

# Solicitando números em loop (10x)

for i in range(10):
    NumP = int(input("Digite aqui um número inteiro para descobrir se é primo: "))
    NumTotal.append(NumP)

# Verificando se é primo

TotalPrimos = 0
for NumP in NumTotal:
    if is_prime(NumP):
        TotalPrimos += 1


# Resposta

print("-=" *28+ "-")
print(f"De todos os dez números digitados, {TotalPrimos} são números primos!")