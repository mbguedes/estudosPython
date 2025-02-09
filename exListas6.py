#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for numero in listaNumeros:
    try:
        soma += numero
    except:
        print("Erro ao somar os números")



listaNumerosError = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a']
for numero in listaNumerosError:
    try:
        soma += numero
    except:
        print("Erro ao somar os números")

print(soma)