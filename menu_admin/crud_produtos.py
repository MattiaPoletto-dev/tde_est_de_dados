from os import system as sys
from classes.classes import Produto
from json_sistema.funcoes_json import salvar_produto_no_json, atualizar_produto_no_json, excluir_produto_do_json

def criar_produto(lista_produtos):
    sys("cls")
    print("-" * 35)
    print(f"{'Criando produto': ^35}\n")

    nome_produto  = input("Nome do produto: ")
    preco_produto = 0
    while True:
        try:
            preco_produto = float(input("Preço do produto: R$ "))
            if preco_produto <= 0:
                raise ValueError
            break
        except ValueError:
            print("\nDigite um número válido!")
            print('-' * 35)
            input("Continuar...")
            sys("cls")
            print("-" * 35)
            print(f"{'Criando produto': ^35}\n")
            print(f"Nome do produto: {nome_produto}")


    produto = {
        "id": Produto.contador_id,
        "nome": nome_produto,
        "preco": preco_produto
    }
    salvar_produto_no_json("json_sistema/dados.json", produto)

    lista_produtos.append(Produto(nome_produto, preco_produto))


    print("\nProduto criado!")
    print("-" * 35)
    input("Continuar...")


def atualizar_produto(lista_produtos):

    if len(lista_produtos) <= 0:
        sys("cls")
        print("-" * 44)
        print("\nNão há produtos cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return None

    while True:
        sys("cls")
        print("-" * 35)
        print(f"{'Atualizando produto': ^35}\n")
        try:
            id_atualizar = int(input("Qual o ID do produto que deseja atualizar? "))
            if id_atualizar < 1:
                raise ValueError
            break
        except ValueError:
            print("\nERRO! Escolha um número inteiro válido")
            print("-" * 35)
            input("Continuar...")

    achou = False
    esquerda = 0
    direita  = len(lista_produtos) - 1
    while esquerda <= direita:
        ponteiro = (esquerda + direita) // 2
        if id_atualizar == lista_produtos[ponteiro].id:
            achou = True
            break
        elif id_atualizar > lista_produtos[ponteiro].id:
            esquerda = ponteiro + 1
        else:
            direita = ponteiro - 1

    if not achou:
        print("\nID não encontrado!")
        print('-' * 35)
        input("Continuar...")
        return None
    
    print("-" * 35)
    print(f"Atualizando o produto: {lista_produtos[ponteiro].nome}\n")
    novo_nome = input("Novo nome ao produto: ")
    novo_preco = 0
    while True:
        try:
            novo_preco = float(input("Novo preço ao produto: R$ "))
            if novo_preco <= 0:
                raise ValueError
            break
        except ValueError:
            print("\nDigite um valor válido!")
            print('-' * 35)
            input("Continuar...")
            sys("cls")
            print("-" * 35)
            print(f"{'Atualizando produto': ^35}\n")
            print(f"Qual o ID do produto que deseja atualizar? {id_atualizar}")
            print("-" * 35)
            print(f"Atualizando o produto: {lista_produtos[ponteiro].nome}\n")
            print(f"Novo nome ao produto: {novo_nome}")
    

    lista_produtos[ponteiro].nome  = novo_nome
    lista_produtos[ponteiro].preco = novo_preco

    atualizar_produto_no_json("json_sistema/dados.json", id_atualizar, novo_nome, novo_preco)

    print("\nProduto atualizado!")
    print("-" * 35)
    input("Continuar...")
    

def remover_produto(lista_produtos):
    if len(lista_produtos) <= 0:
        sys("cls")
        print("-" * 44)
        print("\nNão há produtos cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return None

    while True:
        sys("cls")
        print("-" * 35)
        print(f"{'Excluindo produto': ^35}\n")
        try:
            id_remover = int(input("Qual o ID do produto que deseja remover? "))
            if id_remover < 1:
                raise ValueError
            break
        except ValueError:
            print("\nERRO! Escolha um número inteiro válido")
            print("-" * 35)
            input("Continuar...")

    achou = False
    esquerda = 0
    direita  = len(lista_produtos) - 1
    while esquerda <= direita:
        ponteiro = (esquerda + direita) // 2
        if id_remover == lista_produtos[ponteiro].id:
            achou = True
            break
        elif id_remover > lista_produtos[ponteiro].id:
            esquerda = ponteiro + 1
        else:
            direita = ponteiro - 1

    if not achou:
        print("\nID não encontrado!")
        print("-" * 35)
        input("Continuar...")
        return None
    

    excluir_produto_do_json("json_sistema/dados.json", id_remover)
    lista_produtos.pop(ponteiro)
    print("\nProduto removido!")
    print("-" * 35)
    input("Continuar...")