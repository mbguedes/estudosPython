#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

quadradados =[] 

def cadastrarNumeros():
    numeroInicial = int(input("Digite o número que queira elevar ao quadrado: "))
    numeroQuadrado = numeroInicial ** 2
    quadradados.append({numeroInicial: numeroQuadrado})
    print(f"O número {numeroInicial} elevado ao quadrado é {numeroQuadrado}")

cadastrarNumeros()
