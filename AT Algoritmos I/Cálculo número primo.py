# Exercício número 3

def is_prime(Num):
    if Num < 2:
        return False
    for i in range(2, int(Num ** 0.5) + 1):
        if Num % i == 0:
            return False
    return True

TotalPrimos = []

for Num in range(92, 1479):
    if is_prime(Num):
        TotalPrimos.append(Num)

print("Aqui estão os números primos entre 92 e 1478:")
print()
for i, Primo in enumerate(TotalPrimos):
    print(Primo, end=" ")
    if (i + 1) % 10 == 0:
        print()

print()
print()
print(f"E caso tenha a dúvida, no total tem {len(TotalPrimos)} números primos.")