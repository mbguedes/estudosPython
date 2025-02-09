#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

tabuada = int(input("Digite um número de 1 a 10 para ver a tabuada: "))
for i in range(1,11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")