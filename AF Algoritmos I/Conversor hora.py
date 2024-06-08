# Solicitando os segundos

s = int(input("Digite aqui as horas em segundos: "))

# Conversão

h = int(s / 3600)
m = int((s - (h * 3600)) / 60)
s = int((s - (h * 3600) - (m * 60)))

# Resposta

print ("O resultado é "+str(h)+" hora(s), "+str(m)+" minuto(s) e "+str(s)+" segundo(s)!")
