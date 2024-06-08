# Exercício número 8

# Pedindo idades

idades = []
for i in range(15):
    idade = int(input("Digite aqui a idade: " .format(i+1)))
    idades.append(idade)


total1 = 0
total2 = 0
total3 = 0
total4 = 0

total5 = 0


# Separando faixas etárias

for idade in idades:
    if idade <= 15:
        total1 += 1
    elif idade >15 and idade <=30:
        total2 += 1
    elif idade >30 and idade <=45:
        total3 += 1
    elif idade >45 and idade <=60:
        total4 += 1
    else:
        total5 +=1

# 1° resposta (Faixa etária)

print("As faixas etárias são:")
print("1ª faixa etária = até 15 anos.")
print("2ª faixa etária = de 16 a 30 anos.")
print("3ª faixa etária = de 31 a 45 anos.")
print("4ª faixa etária = de 46 a 60 anos.")
print("5ª faixa etária = com 61 ou mais anos.")

print("-------------------")

print("Tem {} pessoas na primeira faixa etária." .format(total1))
print("Tem {} pessoas na segunda faixa etária." .format(total2))
print("Tem {} pessoas na terceira faixa etária." .format(total3))
print("Tem {} pessoas na quarta faixa etária." .format(total4))
print("Tem {} pessoas na quinta faixa etária." .format(total5))


# 2° resposta (Percentagem)

b = (total1 + total5)
t = (total1 + total2 + total3 + total4 + total5)

p = (b/t) * 100
print("A porcentagem da primeira e da quinta faixa etária combinada é {:.2f}% se comparado as outras faixas etárias." .format(p))