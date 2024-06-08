# Primeira pessoa

nome1 = input("Digite o nome da pessoa 1: ")
idade1 = int(input("Olá, "+str(nome1)+", digite aqui sua idade: "))

# Segunda pessoa

nome2 = input("Digite o nome da pessoa 2: ")
idade2 = int(input("Olá, "+str(nome2)+", digite aqui sua idade: "))

# Os dois juntos

print ("Certo, então {} tem {} anos, enquanto isso {} tem {} anos!".format(nome1, idade1, nome2, idade2))