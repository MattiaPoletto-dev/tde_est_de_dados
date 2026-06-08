import json

def ler_json(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding='utf-8') as arquivo:
        return json.load(arquivo)



def salvar_produto_no_json(caminho_arquivo, produto):
    dados = ler_json(caminho_arquivo)
    dados['produtos'].append(produto)

    with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def atualizar_produto_no_json(caminho_arquivo, id_atualizar, novo_nome, novo_preco):
    dados = ler_json(caminho_arquivo)
    for i, produto in enumerate(dados['produtos']):
        if id_atualizar == produto['id']:
            break
    
    dados['produtos'][i]['nome'] = novo_nome
    dados['produtos'][i]['preco'] = novo_preco

    with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def excluir_produto_do_json(caminho_arquivo, id_remover):
    dados = ler_json(caminho_arquivo)
    
    for i, produto in enumerate(dados['produtos']):
        if id_remover == produto['id']:
            dados['produtos'].pop(i)
            break

    with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)



def salvar_funcionario_no_json(caminho_arquivo, funcionario):
    dados = ler_json(caminho_arquivo)
    dados['usuarios'].append(funcionario)

    with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def atualizar_funcionario_no_json(caminho_arquivo, id_atualizar, novo_login, nova_senha, novo_cpf, novo_nome):
    dados = ler_json(caminho_arquivo)
    for i, usuario in enumerate(dados['usuarios']):
        if id_atualizar == usuario['id']:
            break
    
    dados['usuarios'][i]['login'] = novo_login
    dados['usuarios'][i]['senha'] = nova_senha
    dados['usuarios'][i]['cpf']   = novo_cpf
    dados['usuarios'][i]['nome']  = novo_nome

    with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def excluir_funcionario_do_json(caminho_arquivo, id_remover):

    dados = ler_json(caminho_arquivo)
    
    for i, produto in enumerate(dados['usuarios']):
        if id_remover == produto['id']:
            dados['usuarios'].pop(i)
            break

    with open(caminho_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
