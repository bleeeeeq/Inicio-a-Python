# Solicitando os dados

hrmes = float(input("Digite aqui quantas horas você trabalha por mês: "))
vhrtrab = float(input("Digite aqui o valor que você recebe por hora no trabalho: "))
inss = float(input("Digite aqui a porcentagem do INSS (sem o símbolo %): "))
numd = int(input("Digite aqui a quantia de dependentes abaixo de 14 anos em sua moradia: "))
#sf = float(input("Digite aqui o salário da família: "))

# Cálculo Salário Bruto

sb = (hrmes * vhrtrab)

print (str("O salário bruto é de {} R$" .format (sb)))

# Cálculo Salário Líquido

inss = (inss/ 100)
ins = (sb * inss)

if sb <= 2112.00:
    irrf = 0.0

elif sb <= 2826.65:
    irrf = (sb - ins) * 0.075 - 158.40

elif sb <= 3751.05:
    irrf = (sb - ins) * 0.15 - 370.40

elif sb <= 4664.68:
    irrf = (sb - ins) * 0.225 - 651.73

else:
    irrf = (sb - ins) * 0.275 - 884.96

sl = sb - ins - irrf + 59.82 * numd

print ("O salário líquido é de {:.2f} R$".format(sl))
