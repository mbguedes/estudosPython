#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

lista1 = []
lista2 = []
lista3 = []

lista1 = list(range(1, 11))

for i in range(4):
    nome = input(f"Digite o {i+1}º nome: ") #coleta o nome pedi o {i+1} para que o contador comece do 1 e não do 0, ficando mais natural
    ano_nascimento = int(input(f"Digite o ano de nascimento do {nome}: "))#coleta o ano de nascimento
    lista2.append(nome)
    lista3.append(ano_nascimento)

print("\nLista de números: ", lista1)
print("\nLista de nomes: ", lista2) 
print("Lista de anos de nascimento: ", lista3)