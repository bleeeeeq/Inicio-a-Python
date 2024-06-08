# Exercício número 21

# Solicitando o número e importando a função fatorial para o resultado
# (Apenas por estética do final, já que poderia ter sido direto)

from math import factorial

NumF = int(input("Digite o número que deseja que seja fatorado: "))

F = factorial(NumF)
C = NumF

print("Aqui está o cálculo de {}! ~> ".format(NumF), end="")

while C > 0:
    print("{}".format(C), end="")
    print(" x " if C > 1 else " = ", end="")
    C -= 1
    
print(F)