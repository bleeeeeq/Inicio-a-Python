# Exercício número 7

# Pedindo idades

idades = []
for i in range(10):
    idade = int(input("Digite aqui a idade: " .format(i+1)))
    idades.append(idade)

totali = 0

# Somando idades e dando resposta

for idade in idades:
    if idade > 18:
        totali += 1

print("{} pessoas têm a idade acima de 18 anos." .format(totali))