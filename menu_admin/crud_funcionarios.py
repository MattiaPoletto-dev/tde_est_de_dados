from os import system as sys
from json_sistema.funcoes_json import salvar_funcionario_no_json, atualizar_funcionario_no_json, excluir_funcionario_do_json
from classes.classes import Usuario, No


def altura(no):
    if no is None:
        return 0

    return no.altura

def fator_balanceamento(no):

    if no is None:
        return 0

    return altura(no.esq) - altura(no.dir)

def rotacao_direita(y):

    x = y.esq
    t2 = x.dir

    # Rotação
    x.dir = y
    y.esq = t2

    # Atualiza alturas
    y.altura = 1 + max(
        altura(y.esq),
        altura(y.dir)
    )

    x.altura = 1 + max(
        altura(x.esq),
        altura(x.dir)
    )

    return x

def rotacao_esquerda(x):

    y = x.dir
    t2 = y.esq

    y.esq = x
    x.dir = t2

    x.altura = 1 + max(
        altura(x.esq),
        altura(x.dir)
    )

    y.altura = 1 + max(
        altura(y.esq),
        altura(y.dir)
    )

    return y

def menor_no(no):

    atual = no

    while atual.esq is not None:
        atual = atual.esq

    return atual

def inserir(raiz, usuario):

    if raiz is None:
        return No(usuario)

    if usuario.cpf < raiz.usuario.cpf:
        raiz.esq = inserir(raiz.esq, usuario)

    elif usuario.cpf > raiz.usuario.cpf:
        raiz.dir = inserir(raiz.dir, usuario)

    else:
        return raiz

    # Atualiza altura
    raiz.altura = 1 + max(
        altura(raiz.esq),
        altura(raiz.dir)
    )

    fb = fator_balanceamento(raiz)

    # Rotação simples à direita
    if fb > 1 and usuario.cpf < raiz.esq.usuario.cpf:
        return rotacao_direita(raiz)
    
    # Rotação simples à esquerda
    if fb < -1 and usuario.cpf > raiz.dir.usuario.cpf:
        return rotacao_esquerda(raiz)
    
    # Rotação dupla esquerda-direita
    if fb > 1 and usuario.cpf > raiz.esq.usuario.cpf:
        raiz.esq = rotacao_esquerda(raiz.esq)
        return rotacao_direita(raiz)

    # Rotação dupla direita-esquerda
    if fb < -1 and usuario.cpf < raiz.dir.usuario.cpf:
        raiz.dir = rotacao_direita(raiz.dir)
        return rotacao_esquerda(raiz)

    return raiz

def buscar(raiz, cpf):

    if raiz is None:
        return None
    
    if cpf == raiz.usuario.cpf:
        return raiz.usuario
    
    if cpf < raiz.usuario.cpf:
        return buscar(raiz.esq, cpf)
    
    return buscar(raiz.dir, cpf)

def remover(raiz, cpf):

    if raiz is None:
        return raiz

    # Procurar o nó

    if cpf < raiz.usuario.cpf:
        raiz.esq = remover(raiz.esq, cpf)

    elif cpf > raiz.usuario.cpf:
        raiz.dir = remover(raiz.dir, cpf)

    else:

        # Sem filho esquerdo
        if raiz.esq is None:
            return raiz.dir

        # Sem filho direito
        if raiz.dir is None:
            return raiz.esq

        # Dois filhos
        temp = menor_no(raiz.dir)

        raiz.usuario = temp.usuario

        raiz.dir = remover(
            raiz.dir,
            temp.usuario.cpf
        )

    # Caso a árvore tenha ficado vazia
    if raiz is None:
        return raiz

    # Atualiza altura
    raiz.altura = 1 + max(
        altura(raiz.esq),
        altura(raiz.dir)
    )

    fb = fator_balanceamento(raiz)

    # LL
    if fb > 1 and fator_balanceamento(raiz.esq) >= 0:
        return rotacao_direita(raiz)

    # LR
    if fb > 1 and fator_balanceamento(raiz.esq) < 0:
        raiz.esq = rotacao_esquerda(raiz.esq)
        return rotacao_direita(raiz)

    # RR
    if fb < -1 and fator_balanceamento(raiz.dir) <= 0:
        return rotacao_esquerda(raiz)

    # RL
    if fb < -1 and fator_balanceamento(raiz.dir) > 0:
        raiz.dir = rotacao_direita(raiz.dir)
        return rotacao_esquerda(raiz)

    return raiz

def mostrar_funcionarios_in_order(no):

    if no is None:
        return

    mostrar_funcionarios_in_order(no.esq)

    usuario = no.usuario

    if usuario.role == "func":
        print(f"id    : {usuario.id}")
        print(f"Login : {usuario.login}")
        print(f"Senha : {usuario.senha}")
        print(f"CPF   : {usuario.cpf}")
        print(f"Nome  : {usuario.nome}")
        print("-" * 35)

    mostrar_funcionarios_in_order(no.dir)

def mostrar_funcionarios_pre_order(no):

    if no is None:
        return

    usuario = no.usuario

    if usuario.role == "func":
        print(f"id    : {usuario.id}")
        print(f"Login : {usuario.login}")
        print(f"Senha : {usuario.senha}")
        print(f"CPF   : {usuario.cpf}")
        print(f"Nome  : {usuario.nome}")
        print("-" * 35)

    mostrar_funcionarios_pre_order(no.esq)
    mostrar_funcionarios_pre_order(no.dir)

def mostrar_funcionarios_post_order(no):

    if no is None:
        return

    mostrar_funcionarios_post_order(no.esq)
    mostrar_funcionarios_post_order(no.dir)

    usuario = no.usuario

    if usuario.role == "func":
        print(f"id    : {usuario.id}")
        print(f"Login : {usuario.login}")
        print(f"Senha : {usuario.senha}")
        print(f"CPF   : {usuario.cpf}")
        print(f"Nome  : {usuario.nome}")
        print("-" * 35)


def criar_funcionario(raiz):
    sys("cls")
    print("-" * 35)
    print(f"{'Criando funcionário': ^35}\n")

    login_funcionario = input("Login do funcionário: ")
    senha_funcionario = input("Senha do funcionário: ")
    while True:
        try:
            cpf_funcionario = int(input("CPF do funcionário [somente números]: "))
            
            if buscar(raiz, cpf_funcionario) != None:
                raise ValueError

            if len(str(cpf_funcionario)) != 11:
                raise ValueError
            
            break
        except ValueError:
            print("\nCPF inválido ou já existe!")
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

    raiz = inserir(raiz, Usuario(login_funcionario, senha_funcionario, "func", cpf_funcionario, nome_funcionario))


    print("\nFuncionário criado!")
    print("-" * 35)
    input("Continuar...")
    
    return raiz

def ver_funcionario(raiz, forma_de_ordenacao):

    if raiz is None:
        sys("cls")
        print("-" * 44)
        print("\nNão há usuários cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return

    sys("cls")
    print("*" * 45)
    if forma_de_ordenacao == "1":
        mostrar_funcionarios_in_order(raiz)
    elif forma_de_ordenacao == "2":
        mostrar_funcionarios_pre_order(raiz)
    else:
        mostrar_funcionarios_post_order(raiz)

    print("*" * 45)
    input("Continuar...")

def atualizar_funcionario(raiz):

    if raiz is None:
        print("Não há funcionários cadastrados!")
        input("Continuar...")
        return raiz

    cpf_atualizar = int(input(
        "CPF do funcionário que deseja atualizar [0 para voltar]: "
    ))

    if cpf_atualizar == 0:
        return raiz

    usuario = buscar(raiz, cpf_atualizar)

    if usuario is None:
        print("CPF não encontrado!")
        input("Continuar...")
        return raiz

    print(f"\nAtualizando: {usuario.nome}")

    novo_login = input("Novo login: ")
    nova_senha = input("Nova senha: ")

    while True:
        try:
            novo_cpf = int(input("Novo CPF: "))

            if len(str(novo_cpf)) != 11:
                raise ValueError

            if novo_cpf != usuario.cpf and buscar(raiz, novo_cpf):
                raise ValueError

            break

        except ValueError:
            print("CPF inválido ou já cadastrado!")

    novo_nome = input("Novo nome: ")

    cpf_antigo = usuario.cpf

    raiz = remover(raiz, cpf_antigo)

    usuario.login = novo_login
    usuario.senha = nova_senha
    usuario.cpf   = novo_cpf
    usuario.nome  = novo_nome

    raiz = inserir(raiz, usuario)

    atualizar_funcionario_no_json(
        "json_sistema/dados.json",
        usuario.id,
        novo_login,
        nova_senha,
        novo_cpf,
        novo_nome
    )

    print("\nFuncionário atualizado!")
    input("Continuar...")

    return raiz

def remover_funcionario(raiz):


    if raiz is None:
        sys("cls")
        print("-" * 44)
        print("\nNão há usuários cadastrados!\n")
        print("-" * 44)
        input("Continuar...")
        return raiz

    while True:
        sys("cls")
        print("-" * 35)
        print(f"{'Excluindo funcionário': ^35}\n")

        try:
            cpf_remover = int(
                input("Qual o CPF do funcionário que deseja remover [0 para voltar]? ")
            )

            if cpf_remover == 0:
                return raiz

            break

        except ValueError:
            print("\nERRO! Digite um CPF válido")
            print("-" * 35)
            input("Continuar...")

    usuario = buscar(raiz, cpf_remover)

    if usuario is None:
        print("\nCPF não encontrado!")
        print("-" * 35)
        input("Continuar...")
        return raiz

    excluir_funcionario_do_json(
        "json_sistema/dados.json",
        usuario.id
    )

    raiz = remover(raiz, cpf_remover)

    print("\nFuncionário removido!")
    print("-" * 35)
    input("Continuar...")

    return raiz