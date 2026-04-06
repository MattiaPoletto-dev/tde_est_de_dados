from os import system as sys
from json_sistema.funcoes_json import salvar_funcionario_no_json, atualizar_funcionario_no_json, excluir_produto_do_json
from classes.classes import Usuario
import time

def criar_funcionario(lista_usuarios):
    sys("cls")
    print("-" * 35)
    print(f"{'Criando funcionário': ^35}\n")

    login_funcionario = input("Login do funcionário: ")
    senha_funcionario = input("Senha do funcionário: ")
    while True:
        try:
            cpf_funcionario = int(input("CPF do funcionário [somente números]: "))
            if len(str(cpf_funcionario)) != 11:
                raise ValueError
            break
        except ValueError:
            print("\nDigite um número válido!")
            print('-' * 35)
            input("Continuar...")
            sys("cls")
            print("-" * 35)
            print(f"{'Criando funcionário': ^35}\n")
            print(f"Login do funcionário: {login_funcionario}")
            print(f"Senha do funcionário: {senha_funcionario}")


    nome_funcionario  = input("Nome do funcionário: ")
    

    funcionario = {
        "id"   : Usuario.contador_id,
        "login": login_funcionario,
        "senha": senha_funcionario,
        "role" : "func",
        "cpf"  : cpf_funcionario,
        "nome" : nome_funcionario
    }
    salvar_funcionario_no_json("json_sistema/dados.json", funcionario)

    lista_usuarios.append(Usuario(login_funcionario, senha_funcionario, "func", cpf_funcionario, nome_funcionario))


    print("\nFuncionário criado!")
    print("-" * 35)
    input("Continuar...")

def ver_funcionario(lista_usuarios):
    if len(lista_usuarios) <= 1:
        sys("Cls")
        print("-" * 44)
        print("\nNão há funcionários cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return None

    sys("cls")
    print("*" * 45)
    for usuario in lista_usuarios:
        if usuario.role == "func":
            print(f"id    : {usuario.id}"   )
            print(f"Login : {usuario.login}")
            print(f"Senha : {usuario.senha}")
            print(f"CPF   : {usuario.cpf}"  )
            print(F"Nome  : {usuario.nome}" )
            if usuario != lista_usuarios[-1]:
                print("-" * 35)
            time.sleep(0.25)

    print("*" * 45)
    input("Continuar...")

def atualizar_funcionario(lista_usuarios):
    if len(lista_usuarios) <= 1:
        sys("cls")
        print("-" * 44)
        print("\nNão há funcionários cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return None

    while True:
        sys("cls")
        print("-" * 35)
        print(f"{'Atualizando funcionário': ^35}\n")
        try:
            id_atualizar = int(input("Qual o ID do funcionário que deseja atualizar? "))
            if id_atualizar < 2:
                raise ValueError
            break
        except ValueError:
            print("\nERRO! Escolha um número inteiro válido")
            print("-" * 35)
            input("Continuar...")

    achou = False
    esquerda = 0
    direita  = len(lista_usuarios) - 1
    while esquerda <= direita:
        ponteiro = (esquerda + direita) // 2
        if id_atualizar == lista_usuarios[ponteiro].id:
            achou = True
            break
        elif id_atualizar > lista_usuarios[ponteiro].id:
            esquerda = ponteiro + 1
        else:
            direita = ponteiro - 1

    if not achou:
        print("\nID não encontrado!")
        print('-' * 35)
        input("Continuar...")
        return None
    
    print("-" * 35)
    print(f"Atualizando o funcionário: {lista_usuarios[ponteiro].nome}\n")

    novo_login = input("Novo login do usuário: ")
    nova_senha = input("Nova senha do funcionário: ")

    novo_cpf = 0
    while True:
        try:
            novo_cpf = int(input("Novo CPF do funcionário: "))
            if len(str(novo_cpf)) != 11 or novo_cpf < 0:
                raise ValueError
            break
        except ValueError:
            print("\nDigite um valor válido!")
            print('-' * 35)
            input("Continuar...")
            sys("cls")
            print("-" * 35)
            print(f"{'Atualizando funcionário': ^35}\n")
            print(f"Qual o ID do funcionário que deseja atualizar? {id_atualizar}")
            print("-" * 35)
            print(f"Atualizando o funcionário: {lista_usuarios[ponteiro].nome}\n")
            print(f"Novo login do usuário: {novo_login}")
            print(f"Nova senha do funcionário: {nova_senha}")
    
    novo_nome = input("Novo nome do funcionário: ")

    lista_usuarios[ponteiro].login = novo_login
    lista_usuarios[ponteiro].senha = nova_senha
    lista_usuarios[ponteiro].cpf   = novo_cpf
    lista_usuarios[ponteiro].nome  = novo_nome

    atualizar_funcionario_no_json("json_sistema/dados.json", id_atualizar, novo_login, nova_senha, novo_cpf, novo_nome)

    print("\nFuncionário atualizado!")
    print("-" * 35)
    input("Continuar...")

def remover_funcionario(lista_usuarios):
    if len(lista_usuarios) <= 1:
        sys("cls")
        print("-" * 44)
        print("\nNão há usuários cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return None

    while True:
        sys("cls")
        print("-" * 35)
        print(f"{'Excluindo funcionpario': ^35}\n")
        try:
            id_remover = int(input("Qual o ID do funcionário que deseja remover? "))
            if id_remover < 2:
                raise ValueError
            break
        except ValueError:
            print("\nERRO! Escolha um número inteiro válido")
            print("-" * 35)
            input("Continuar...")

    achou = False
    esquerda = 0
    direita  = len(lista_usuarios) - 1
    while esquerda <= direita:
        ponteiro = (esquerda + direita) // 2
        if id_remover == lista_usuarios[ponteiro].id:
            achou = True
            break
        elif id_remover > lista_usuarios[ponteiro].id:
            esquerda = ponteiro + 1
        else:
            direita = ponteiro - 1

    if not achou:
        print("\nID não encontrado!")
        print("-" * 35)
        input("Continuar...")
        return None
    

    excluir_produto_do_json("json_sistema/dados.json", id_remover)
    lista_usuarios.pop(ponteiro)
    print("\nFuncionário removido!")
    print("-" * 35)
    input("Continuar...")