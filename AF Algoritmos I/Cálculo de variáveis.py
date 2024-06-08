# Solicitando as informações

produto = str(input("Digite o produto: "))
qntd = int(input("Digite a quantidade desse mesmo produto: "))
VU = int(input("Digite o valor unitário desse mesmo produto: "))

# Cálculo

VT = (qntd * VU)

# Resultado

print ("Certo, o valor total de "+(produto)+" é "+str(VT))