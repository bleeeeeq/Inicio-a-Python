# Valores a, b e c

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

#  Delta e raiz

dt = (b**2 - 4*a*c)

raiz = (dt)**0.5

# X1 e X2

x1 = (-b + raiz)/(2*a)
x2 = (-b - raiz)/(2*a)

# Respostas

print ("O Valor de delta é " +str(dt)+".")

if (dt) <0: print ("Delta é menor que zero, logo, as raízes não são reais!")
elif (dt) ==0: print ("O valor dessa equação é " +str(x1) +".")
else : print ("As raízes dessa equação são " +str(x1) +" e " +str(x2))