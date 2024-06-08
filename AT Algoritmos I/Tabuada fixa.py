# Exercício número 10

# Criando o loop e dando a resposta direta

for num in range (1,11):
    print("-=" *11+"-")
    print()
    print(f"A tabuada do número {num}:")
    print()
    for i in range (1,11):
        res = num * i
        print(f"{num} x {i} = {res}")
    print()