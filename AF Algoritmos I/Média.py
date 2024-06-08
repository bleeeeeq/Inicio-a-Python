# Primeira Pessoa

nome1 = input("Nome da primeira pessoa: ")
idade1 = int(input("Idade do(a) " +(str(nome1)) +": "))

# Segunda Pessoa

nome2 = input("Nome da segunda pessoa: ")
idade2 = int(input("Idade do(a) " +(str(nome2)) +": "))

# Terceira Pessoa

nome3 = input("Nome da terceira pessoa: ")
idade3 = int(input("Idade do(a) " +(str(nome3)) +": "))

# Quarta Pessoa

nome4 = input("Nome da quarta pessoa: ")
idade4 = int(input("Idade do(a) " +(str(nome4)) + ": "))

# Média final

média = (idade1 + idade2 + idade3 + idade4) / 2
print ("A média entre as idades de todas as pessoas citadas é de {}" .format(média))
