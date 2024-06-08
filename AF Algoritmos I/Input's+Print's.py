# Solicitando das informações

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura (em centímetros): "))
profissão = input("Digite a profissão que você trabalha: ")
rua = input("Digite o nome da rua que você mora: ")
bairro = input("Digite o nome do bairro que você mora: ")
cidade = input("Digite o nome da cidade que você mora: ")
estado = input("Digite o nome do estado que você mora: ")
cep = int(input("Digite o CEP do local que você mora: "))
telefone = int(input("Digite o número do seu telefone: "))

# Devolvendo as informações

print ("Olá, " +nome + "! Aqui estão suas informações:")
print ("Sua idade é: "+str(idade) +" anos;")
print ("Você se identifica no sexo " +sexo +";")
print ("Você pesa: "+str(peso) +"kg;")
print ("Sua altura é: "+str(altura) +"cm;")
print ("Você trabalha como "+profissão +";")
print ("Você mora na "+rua + ", bairro " +bairro + ", " +cidade +", em "+estado+";")
print ("O seu CEP é: "+str(cep) +";")
print ("E o seu número é: "+str(telefone) +";")