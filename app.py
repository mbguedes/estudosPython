import os

restaurantes = [
    {'nome': 'Viana', 'categoria': 'Frutos do Mar', 'ativo': False},
    {'nome': 'Burguer King', 'categoria': 'Fast Food', 'ativo': True},
    {'nome': 'McDonalds', 'categoria': 'Fast Food', 'ativo': True}
]


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Finalizando o programa")

def voltar_ao_menu_principal():
    print("\nPressione uma tecla para voltar ao menu principal. ")
    input()
    main()

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    print(f'{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(20)} | {"Estado"}')
    for restaurante in restaurantes:  
        nome_restaurante = restaurante['nome']  # Acessa a chave 'nome' do dicionário
        categoria_restaurante = restaurante['categoria']  # Acessa a chave 'categoria'
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'  # Acessa a chave 'ativo'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternarnando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar restaurantes')
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

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

if __name__ == "__main__":
    main() 