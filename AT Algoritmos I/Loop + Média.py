# Exercício número 26

Soma = Total = 0

# Loop com quebra na idade "0"

while True:
    Idade = int(input("Digite sua idade [Digite 0 para finalizar]: "))
    if Idade == 0:
        break

    Total += 1
    Soma += Idade

# Cálculo da média e resposta

Media = (Soma / Total)
print(f"A média das idades dadas acima é de {Media:.2f}")