# Primeira pessoa

nome1 = input("Digite o nome da primeira pessoa: ")
print ("Prazer, {}!" .format(nome1))
idade1 = int(input("Agora, {}, digite sua idade: ".format(nome1)))

print ("Ótimo! Vamos para a segunda pessoa!")

# Segunda Pessoa

nome2 = input("Agora digite o nome da segunda pessoa: ")
print ("Prazer, {}! Também irei precisar da sua idade!" .format(nome2))
idade2 = int(input("Então, {}, digite aqui sua idade: ".format(nome2)))

# Resultado

print ("Tudo certo, agora vamos fazer a diferença e a soma das duas idades.")
s1 = idade1 - idade2
print ("A diferença entre {} e {} é igual a {}." .format(idade1, idade2, s1))


s2 = idade1 + idade2
print ("Já a soma das duas idades resulta em {}." .format(s2))