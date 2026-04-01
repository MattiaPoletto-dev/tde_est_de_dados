from menu_admin.crud_funcionarios import criar_funcionario, ver_funcionario, atualizar_funcionario, remover_funcionario
from menu_admin.crud_produtos import criar_produto, ver_produto, atualizar_produto, remover_produto
from menu_funcionario.area_funcionario import chamar_proximo_da_fila, ver_historico_de_compras, ver_produtos, ver_produto_especifico
from classes.classes import Usuario, Funcionario, Produto
import json, time


# Funções menus

def menu_login(lista_usuarios): # Retorna o objeto se condizer com o login e senha, retorna None se não condizer
    return None


# ----------------------------------------------------
def menu_admin():
    while True:
        print("Painel administrador\n")
        print("1. Gestão de funcionários")
        print("2. Gestão de produtos")
        print("0. Sair")
        escolha = input("Escolha: ")

        if escolha == "0":
            print("Saindo...")
            time.sleep(2)
            break
        elif escolha == "1":
            gestao_funcionarios()
        elif escolha == "2":
            gestao_produtos()
        else:
            print("ERRO! Escolha inválida")

def gestao_funcionarios():
    while True:
        print("Gestão de funcionários\n")
        print("1. Criar funcionário")
        print("2. Ver funcionário")
        print("3. Atualizar dados do funcionário")
        print("4. Remover funcionário")
        print("0. Sair")
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            criar_funcionario()
        elif escolha == "2":
            ver_funcionario()
        elif escolha == "3":
            atualizar_funcionario()
        elif escolha == "4":
            remover_funcionario()
        else:
            print("ERRO! Escolha inválida")

def gestao_produtos():
    while True:
        print("Gestão de produtos\n")
        print("1. Criar produto")
        print("2. Ver produto")
        print("3. Atualizar dados do produto")
        print("4. Remover produto")
        print("0. Sair")
        escolha = input("Escolha: ")
        if escolha == "0":
            break
        elif escolha == "1":
            criar_produto()
        elif escolha == "2":
            ver_produto()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            remover_produto()
        else:
            print("ERRO! Escolha inválida")


# ----------------------------------------------------
def menu_funcionario():
    while True:
        print("Painel funcionário\n")
        print("1. Chamar o próximo da fila")
        print("2. Ver histórico de compras")
        print("3. Ver produtos")
        print("4. Procurar produto específico")
        print("0. Sair")
        escolha = input("Escolha: ")

        if escolha == "0":
            print("Saindo...")
            time.sleep(2)
            break
        elif escolha == "1":
            chamar_proximo_da_fila()
        elif escolha == "2":
            ver_historico_de_compras()
        elif escolha == "3":
            ver_produtos()
        elif escolha == "4":
            ver_produto_especifico()
        else:
            print("ERRO! Escolha inválida")



# Dados do json para o programa
with open("json/dados.json", "r", encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


lista_usuarios = []
for usuario in dados['usuarios']:
    lista_usuarios.append(Usuario(usuario['login'], usuario['senha'], usuario['role']))

lista_funcionarios = []
for funcionario in dados['usuarios']:
    if funcionario['role'] == "func":
        lista_funcionarios.append(Funcionario(funcionario['cpf'], funcionario['nome']))

lista_produtos = []
for produto in dados['produtos']:
    lista_produtos.append(Produto(produto['id'], produto['nome'], produto['preco']))



# Programa rodando
while True:
    usuario_autenticado = menu_login(lista_usuarios)

    if usuario_autenticado is None:
        print("Usuário ou senha incorretos")
    else:
        if usuario_autenticado.role == "admin":
            menu_admin()
        elif usuario_autenticado.role == "funcionario":
            menu_funcionario()
        else:
            print("ERRO na role deste usuário, favor contatar o suporte!")