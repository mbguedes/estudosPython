# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

listaNumeros = [1, 2, 3, 4, 10]
soma = 0
for numero in listaNumeros:
    soma += numero

media = soma / len(listaNumeros)

print("A média dos números da lista é: ", media)

