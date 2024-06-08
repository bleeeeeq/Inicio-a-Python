# Exercício número 9

# Pedindo o número

num = int(input("Digite aqui o número que deseja saber a tabuada: "))

# Cálculo e resposta

print ("-----------")
for i in range (1,11):
    res = (num * i)

    print(num, "x", i, "=", res)

print ("-----------")