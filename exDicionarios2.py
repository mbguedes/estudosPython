#2 - Utilizando o dicionário criado no item 1:

#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.
import os

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

def exibir_opcoes():
    print('1. Alterar nome da pessoa')
    print('2. Alterar idade da pessoa')
    print('3. Listar pessoas')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    print("\nPressione uma tecla para voltar ao menu principal. ")
    input()
    main()

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_ao_menu_principal()

def alterarNome(pessoas, nome, novo_nome):
    for pessoa in pessoas:
        if pessoa["nome"] == nome:
            pessoa["nome"] = novo_nome
            return
    print("Nome não encontrado")

def alterarIdade(pessoas, nome, nova_idade):
    for pessoa in pessoas:
        if pessoa["nome"] == nome:
            pessoa["idade"] = nova_idade
            print(f"Idade de {nome} alterada para {nova_idade}.")
            return
    print(f"Nome '{nome}' não encontrado.")

def exibir_nome_do_programa():
    print("Sistema de teste de dicionários\n")

def finalizar_app():
    exibir_subtitulo("Finalizando o programa")

def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def listar_pessoas():
    exibir_subtitulo('Listando pessoas')
    print(f'{"Nome da Pessoa".ljust(23)} | {"Idade".ljust(20)} | {"Cidade"}')
    for pessoa in pessoas:  
        nome_pessoa = pessoa['nome']  # Acessa a chave 'nome' do dicionário
        idade_pessoa = pessoa['idade']  # Acessa a chave 'idade'
        cidade = pessoa['cidade']  # Acessa a chave 'cidade'
        print(f' - {nome_pessoa.ljust(20)} | {str(idade_pessoa).ljust(20)} | {cidade}')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Alterando nome da pessoa')
            nome = input("Digite o nome da pessoa que deseja alterar: ")
            novo_nome = input("Digite o novo nome: ")
            alterarNome(pessoas, nome, novo_nome)
            voltar_ao_menu_principal()

        elif opcao_escolhida == 2:
            print('Alterar idade da pessoa')
            nome = input("Digite o nome da pessoa que deseja alterar a idade: ")
            nova_idade = int(input("Digite a nova idade: "))
            alterarIdade(pessoas, nome, nova_idade)
            voltar_ao_menu_principal()

        elif opcao_escolhida == 3:
            print('Listar pessoas')
            listar_pessoas()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()  