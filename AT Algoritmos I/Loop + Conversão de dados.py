# Exercício número 24

# Dados iniciais

TMas = TMasS = TMasN = 0
TFem = TFemS = TFemN = 0
TS = TN = 0

# Solicitando os dados e mantendo um loop caso escreva errado

for i in range(1, 11):
    print("Pessoa ", i)

    Gostou = str(input("Gostou do novo produto? [S - N]: ")).strip().upper()[0]
    while Gostou not in "SN":
        Gostou = str(input("Gostou do novo produto? [S - N]: ")).strip().upper()[0]
    if Gostou == "S":
        TS += 1
    if Gostou == "N":
        TN += 1

    Sexo = str(input("Masculino ou Feminino? [M - F]: ")).strip().upper()[0]
    while Sexo not in "MF":
        Sexo = str(input("Masculino ou Feminino? [M - F]: ")).strip().upper()[0]
    if Sexo == "M":
        TMas += 1
    if Sexo == "F":
        TFem += 1

    print()

# Conversão de dados

    if Sexo == "F" and Gostou == "S":
        TFemS += 1
    if Sexo == "M" and Gostou == "N":
        TMasN += 1

TMasSP = (TMasN / TMas) * 100

# Respostas

print("-----------------------------------")
print()
print("Um total de {} pessoas responderam com \"SIM\".".format(TS))
print("Um total de {} pessoas responderam com \"NÃO\".".format(TN))
print()
print("De {} mulheres, {} responderam com \"SIM\".".format(TFem,TFemS))
print("De {} homens, a porcentagem de negação foi de {:.2f}%.".format(TMas,TMasSP))
print()
print("-----------------------------------")