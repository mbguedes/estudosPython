#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

somaImpares = 0
for i in range(1, 11):
    if i % 2 != 0:
        somaImpares += i

print(somaImpares)