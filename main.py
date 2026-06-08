from menu_admin.crud_funcionarios import criar_funcionario, ver_funcionario, atualizar_funcionario, remover_funcionario, inserir
from menu_admin.crud_produtos import criar_produto, atualizar_produto, remover_produto
from menu_funcionario.area_funcionario import ver_fila, chamar_proximo_da_fila, ver_historico_de_compras, ver_historico_ordenado_preco, cancelar_ultima_compra,ver_produtos, ver_produto_especifico
from json_sistema.funcoes_json import ler_json
from classes.classes import Usuario, Produto
import time, getpass, random
from os import system



# ----------------------------------------------------
#                    Funções menus
# ----------------------------------------------------

def menu_login(lista_usuarios): # Retorna o objeto se condizer com o login e senha, retorna None se não condizer
    login_input = input("Usuário: ").strip()
    
    senha_input = getpass.getpass("Senha: ")

    for usuario in lista_usuarios:
        if usuario.login == login_input and usuario.senha == senha_input:
            print(f"\nBem-vindo, {usuario.login}")
            print("-" * 35)
            input("Continuar...")
            return usuario
    
    print("\nUsuário ou senha incorretos")
    print("-" * 35)
    input("Continuar...")
    return None


# --------------------- ADMIN -------------------------
def menu_admin():
    while True:
        system("cls")
        print("-" * 35)
        print(f"{'Painel administrador': ^35}\n")
        print("1. Gestão de funcionários")
        print("2. Gestão de produtos")
        print("0. Sair")
        escolha = input("Escolha: ")

        if escolha == "0":
            print("\nSaindo...")
            time.sleep(2)
            break
        elif escolha == "1":
            gestao_funcionarios()
        elif escolha == "2":
            gestao_produtos()
        else:
            print("\nERRO! Escolha inválida")
            print("-" * 35)
            input("Continuar...")

def gestao_funcionarios():
    global raiz

    while True:
        system("cls")
        print("-" * 35)
        print(f"{'Gestão de funcionários': ^35}\n")
        print("1. Criar funcionário")
        print("2. Ver funcionários")
        print("3. Atualizar dados do funcionário")
        print("4. Remover funcionário")
        print("0. Voltar")
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            raiz = criar_funcionario(raiz)
        elif escolha == "2":
            while True:
                print()
                print("-" * 52)
                print("1. In order")
                print("2. Pre order")
                print("3. Post order")
                forma_de_ordenacao = str(input("Escolha: "))
                if forma_de_ordenacao in ["1", "2", "3"]:
                    break
            
            ver_funcionario(raiz, forma_de_ordenacao)
        elif escolha == "3":
            raiz = atualizar_funcionario(raiz)
        elif escolha == "4":
            raiz = remover_funcionario(raiz)
        else:
            print("\nERRO! Escolha inválida")
            print("-" * 35)
            input("Continuar...")

def gestao_produtos():
    while True:
        system("cls")
        print("-" * 35)
        print(f"{'Gestão de produtos': ^35}\n")
        print("1. Criar produto")
        print("2. Ver produtos")
        print("3. Atualizar dados do produto")
        print("4. Remover produto")
        print("0. Voltar")
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            criar_produto(lista_produtos)
        elif escolha == "2":
            ver_produtos(lista_produtos)
        elif escolha == "3":
            atualizar_produto(lista_produtos)
        elif escolha == "4":
            remover_produto(lista_produtos)
        else:
            print("\nERRO! Escolha inválida")
            print("-" * 35)
            input("Continuar...")



# ------------------- FUNCIONÁRIO ---------------------
def menu_funcionario():
    while True:
        system("cls")
        print("-" * 35)

        if not fila:
            while True:
                cliente_entrando_na_fila(fila,lista_produtos)
                if len(fila) >= 7:
                    break

        print(f"{'Painel funcionário': ^35}\n")
        print("1. Ver fila")
        print("2. Chamar o próximo da fila")
        print("3. Ver histórico de compras")
        print("4. Ver histórico de compras ordenado por menor preço")
        print("5. Cancelar última compra")
        print("6. Ver produtos")
        print("7. Procurar produto específico")
        print("0. Sair")
        escolha = input("Escolha: ")

        if escolha == "0":
            print("\nSaindo...")
            time.sleep(2)
            break
        elif escolha == "1":
            ver_fila(fila)
        elif escolha == "2":
            chamar_proximo_da_fila(fila, historico_de_compras)
            cliente_entrando_na_fila(fila,lista_produtos)
        elif escolha == "3":
            ver_historico_de_compras(historico_de_compras)
        elif escolha == "4":
            ver_historico_ordenado_preco(historico_de_compras)
        elif escolha == "5":
            cancelar_ultima_compra(historico_de_compras)
        elif escolha == "6":
            ver_produtos(lista_produtos)
        elif escolha == "7":
            indice = ver_produto_especifico(lista_produtos)
            if indice == -1:
                print("\nProduto não encontrado!")
                print("*" * 35)
                input("Continuar...")
            elif indice == -2:
                pass
            else:
                print("-" * 25)
                print(f"ID   : {lista_produtos[indice].id}")
                print(f"Nome : {lista_produtos[indice].nome}")
                print(f"Preço: R${lista_produtos[indice].preco:.2f}\n")
                print("*" * 35)
                input("Continuar...")
        else:
            print("\nERRO! Escolha inválida")
            print("-" * 35)
            input("Continuar...")

def cliente_entrando_na_fila(fila,lista_produtos):
    valor = random.randint(1,100)
    if valor > 75:
        prioridade = random.randint(0,1)
        compras = []
        indices_produtos = []
        for _ in range(len(lista_produtos)):
            indice = random.randint(0,len(lista_produtos)-1)
            if indice not in indices_produtos:
                indices_produtos.append(indice)

        for indice in indices_produtos:
            compra = (lista_produtos[indice], random.randint(1,5))
            compras.append(compra)
        
        cliente = {
            "prioridade": prioridade,
            "compras"   : compras
        }

        fila.append(cliente)
        ordenar_lista_por_prioridade(fila)

def ordenar_lista_por_prioridade(fila):
    for i in range(1, len(fila)):
        
        for j in range(i, 0, -1):
            if fila[j]["prioridade"] < fila[j-1]["prioridade"]:
                obj = fila[j]
                fila[j] = fila[j-1]
                fila[j-1] = obj
            else:
                break

    return fila





# ----------------------------------------------------
#            Dados do json para o programa
# ----------------------------------------------------
dados = ler_json("json_sistema/dados.json")


lista_usuarios = []
lista_produtos = []
fila = []
historico_de_compras = []



raiz = None
for user in dados['usuarios']:
    usuario = Usuario(user['login'], user['senha'], user['role'], user['cpf'], user['nome'])

    lista_usuarios.append(usuario)
    
    raiz = inserir(raiz, usuario)


for produto in dados['produtos']:
    lista_produtos.append(Produto(produto['nome'], produto['preco']))





# ----------------------------------------------------
#                  Programa rodando
# ----------------------------------------------------
while True:
    system("cls")
    print("-" * 35)
    print(f"{'Login sistema': ^35}\n")
    usuario_autenticado = menu_login(lista_usuarios)
        
    if usuario_autenticado is not None:
        if usuario_autenticado.role == "admin":
            menu_admin()
        elif usuario_autenticado.role == "func":
            menu_funcionario()
        else:
            print("ERRO na role deste usuário, favor contatar o suporte!")
            print("-" * 35)
            input("Continuar...")
