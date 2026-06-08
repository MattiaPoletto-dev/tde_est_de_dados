class Usuario:
    contador_id = 1

    def __init__(self, login, senha, role, cpf, nome):
        self.id    = Usuario.contador_id
        Usuario.contador_id += 1
        self.login = login
        self.senha = senha
        self.role  = role
        self.cpf   = cpf
        self.nome  = nome


class Produto:
    contador_id = 1

    def __init__(self, nome, preco):
        self.id = Produto.contador_id
        Produto.contador_id += 1
        self.nome  = nome
        self.preco = preco


class No:
    def __init__(self, usuario):
        self.usuario = usuario
        self.esq = None
        self.dir = None
        self.altura = 1