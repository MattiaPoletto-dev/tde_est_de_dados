class Usuario:
    def __init__(self, login, senha, role):
        self.login = login
        self.senha = senha
        self.role  = role

class Funcionario:
    def __init__(self, cpf, nome):
        self.cpf  = cpf
        self.nome = nome

class Produto:
    def __init__(self, id, nome, preco):
        self.id    = id
        self.nome  = nome
        self.preco = preco