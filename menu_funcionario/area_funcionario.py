from os import system as sys
import time

def ver_fila(fila):
    sys("cls")
    print("-" * 35)
    print("Fila:\n")
    for i, cliente in enumerate(fila):
        print(f"Cliente {i+1}")
        print(f"Prioridade: {cliente['prioridade']}\n")
    input("Continuar...")

def chamar_proximo_da_fila(fila, historico):
    sys("cls")

    proximo = fila.pop(0)
    print("Passando compras...\n")
    print("*" * 44)
    total_compra = 0
    for compra in proximo['compras']:
        total_compra += (compra[0].preco * compra[1])
        for _ in range(compra[1]):
            print(f"  {compra[0].nome: <30} - R$ {(compra[0].preco): >5.2f}")
            time.sleep(0.5)
    print("-" * 44)
    print(f"  Total                          - R$ {total_compra:.2f}")
    time.sleep(2)
    print("  Pagando...")
    time.sleep(3)
    print("  Compra realizada!")
    print("*" * 44)
    time.sleep(2)

    historico.append((proximo['compras'], total_compra))
    input("Continuar...")

    return proximo


def ver_historico_de_compras(historico):
    sys("cls")

    if len(historico) <= 0:
        print("-" * 44)
        print("O histórico está vazio!\n")
        input("Continuar...")
        return None
    
    print("Compras realizadas:\n")
    print("-" * 44)

    for i in range(len(historico)-1, -1, -1):
        print("-" * 15)
        print(f"Compra {i+1}\n")
        for produto, quantidade in historico[i][0]:
            print(f"Produto   : {produto.nome}")
            print(f"Quantidade: {quantidade}")
        print(f"\nTotal da compra: R${historico[i][1]:.2f}\n")

    print("-" * 44)
    input("Continuar...")

def cancelar_ultima_compra(historico):
    sys("cls")

    if len(historico) <= 0:
        print("-" * 44)
        print("O histórico está vazio!\n")
        input("Continuar...")
        return None
    
    compra = historico.pop()
    print("-" * 44)
    print("Última compra apagada com sucesso!\n")
    input("Continuar...")
    return compra

def ver_produtos(lista_produtos):
    if len(lista_produtos) <= 0:
        sys("cls")
        print("-" * 44)
        print("\nNão há produtos cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return None
    
    sys("cls")
    print("*" * 45)

    for produto in lista_produtos:
        print(f"id    : {produto.id}")
        print(f"Nome  : {produto.nome}")
        print(F"Preço : R$ {produto.preco:.2f}")
        if produto != lista_produtos[-1]:
            print("-" * 35)
        time.sleep(0.25)

    print("*" * 45)
    input("Continuar...")

def ver_produto_especifico(lista_produtos):
    while True:
        sys("cls")
        print("Deseja buscar de qual forma?\n")
        print("1. ID")
        print("2. Nome")
        print("0. Voltar ")
        escolha = input("Escolha: ")
        if escolha not in ["0","1","2"]:
            print("\nERRO! Escolha inválida")
            print("-" * 35)
            input("Continuar...")
        else:
            sys("cls")
            break
    
    match escolha:
        case "1":
            while True:
                try:
                    sys("cls")
                    print()
                    print("*" * 35, "\n")
                    indice_procurado = int(input("ID do produto: "))
                    break
                except ValueError:
                    print("\nERRO! Somente são aceitos números inteiros")
                    print("-" * 35)
                    input("Continuar...")

            
            if indice_procurado < 0 or indice_procurado > len(lista_produtos):
                return -1

            esquerda = 0
            direita  = len(lista_produtos) - 1
            while esquerda <= direita:
                ponteiro = (esquerda + direita) // 2
                if indice_procurado == lista_produtos[ponteiro].id:
                    return ponteiro
                elif indice_procurado > lista_produtos[ponteiro].id:
                    esquerda = ponteiro + 1
                else:
                    direita = ponteiro - 1
            
            return -1

        case "2":
            sys("cls")
            print()
            print("*" * 35, "\n")
            nome_procurado = input("Nome do produto: ")
            for i, produto in enumerate(lista_produtos):
                if nome_procurado.strip().lower() == produto.nome.strip().lower():
                    return i
            return -1

        case "0":
            return -2
