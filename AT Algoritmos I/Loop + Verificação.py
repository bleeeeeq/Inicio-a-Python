# Exercício número 15

# Criei um loop que acaba previnindo de utilizar letras, só aceitando números

Cont = 0
for i in range (1,11):
    Num = input(f"Digite o {i}° número: ")
    while True:
        if Num.isdigit():
            Num = float(Num)
            break
        else:
            Num = input(f"Digite o {i}° número: ")

    if Num > 30 and Num < 90:
        Cont += 1

print(f"Dos 10 números digitados, {Cont} estão entre 30 e 90.")