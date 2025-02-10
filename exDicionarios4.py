#4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoas = [
    {
        "nome": "Ana Silva",
        "idade": 29,
        "cidade": "São Paulo"
    },
    {
        "nome": "Carlos Pereira",
        "idade": 34,
        "cidade": "Rio de Janeiro"
    },
    {
        "nome": "Beatriz Souza",
        "idade": 22,
        "cidade": "Belo Horizonte"
    },
    {
        "nome": "Daniela Oliveira",
        "idade": 40,
        "cidade": "Brasília"
    },
    {
        "nome": "Eduardo Santos",
        "idade": 27,
        "cidade": "Curitiba"
    }
]


def verificarChave(dicionario, chave):
    if chave in dicionario:
        print(f"A chave '{chave}' existe no dicionário.")
    else:
        print(f"A chave '{chave}' não existe no dicionário.")

def exibirMenu():
    print("Menu: ")
    print("1. Verificar se uma chave existe no dicionário.")
    print("2. Sair.")

def main():
    while True:
        exibirMenu()
        opcao = input("Digite uma opção: ")

        if opcao == "1":
            chave = input("Digite a chave que deseja verificar: ")
            verificarChave(pessoas[0], chave)
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione uma tecla para tentar novamente...")
            
if __name__ == '__main__':
    main()