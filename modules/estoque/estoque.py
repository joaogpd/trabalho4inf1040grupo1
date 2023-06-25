from ctypes import *
import os

__all__ = ["remove_jogo", "exibe_todos_estoque", "exibe_jogo", "inserir_jogo", "diminuir_quantidade", "aumentar_quantidade"]

def validaArg(func):
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            print(f"Error, função {func.__name__} não recebeu argumentos")
        return func(*args, **kwargs)
    return wrapper

"""
** Objetivo: remover um jogo da estrutura estoque
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Confere se o valor está na estrutura
- Remove esse valor da estrutura
** Acoplamento
* Parâmetro:
- nome -> str: nome do jogo a ser removido
- estrutura -> dict: estrutura de estoque
* Retornos:
- -1: caso de 'nome' não ser str
- 0: caso de jogo não encontrado
- 1: caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe dois parâmetros
* Assertivas de saída:
- O valor passado é removido da estrutura
"""
@validaArg
def remove_jogo(nome, estrutura):
    if not isinstance(nome, str):
        return -1 # Nome invalido
    if nome in estrutura:
        del estrutura[nome]
        return 1 # Jogo removido com sucesso
    return 0 # Jogo nao encontrado (já removido)

"""
** Objetivo: exibir todos os itens da estrutura estoque
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Confere se a estrutura está vazia
- Imprime todos as chaves presentes na estrutura
** Acoplamento
* Parâmetro:
- estrutura -> dict: estrutura que deve ter chaves impressas
* Retornos:
- -8: caso de 'estrutura' não ser dict
- -9: caso de 'estrutura' estar vazia
- 1: caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe um parâmetro
* Assertivas de saída:
- Todos as chaves da estrutura foram impressas
"""
@validaArg
def exibe_todos_estoque(estrutura):
  if not isinstance(estrutura, dict):
    return -8
  if not estrutura:
    return -9 # Estrutura vazia. Dicionario vazio "valued" como "false"
  for i in estrutura.keys():
    print("Nome: {}".format(i))
  return 1

"""
** Objetivo: exibir informação de um item presente no estoque
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Confere se a estrutura está vazia
- Imprime a chave desejada e a sua quantidade
** Acoplamento
* Parâmetro:
- nome -> string com o nome do jogo a ser impresso
- estrutura -> dict: estrutura que deve ter chaves impressas
* Retornos:
- -11: caso de 'nome' não ser string
- -8: caso de 'estrutura' não ser dict
- -9: caso de 'estrutura' estar vazia
- 1: caso de sucesso
- 0: caso de jogo não encontrado
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe dois parâmetros
* Assertivas de saída:
- As informações desejadas serão impressas
"""
@validaArg
def exibe_jogo(nome, estrutura):
    if not isinstance(nome, str):
        return -11 # Nome inválido
    if not isinstance(estrutura, dict):
        return -8 # Estrutura inválida
    if not estrutura:
        return -9 # Estrutura vazia
    if nome in estrutura:
        print("Nome: " + nome + "\nQuantidade:", estrutura[nome])
        return 1 # Jogo existente
    else:
        return 0 # Jogo não encontrado
    
"""
** Objetivo: inserir unidades de um jogo no estoque
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Atualiza o dicionário estrutura com a quantiade correta
** Acoplamento
* Parâmetro:
- estrutura -> dict: estrutura que deve ter conteúdo impresso em totalidade
- nome -> string: nome do jogo que deve ter a quantidade atualizada
* Retornos:
- -4: caso de 'estrutura' não ser dict
- -5: caso de 'quantidade' não ser int ou 'nome' não ser string
- 1: em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor correto da quantidade
"""
@validaArg
def inserir_jogo(estrutura, nome, quantidade=10):
    # Tratando casos de parametros invalidos
    if not isinstance(estrutura, dict):
        # print("Erro, a estrutura passada não é dict")
        return -4
    if not isinstance(quantidade, int):
        # print("Erro, a quantidade passada não é inteira")
        return -5
    if not isinstance(nome, str):
        # print("Erro, o nome não é uma string")
        return -5
    estrutura[nome] = quantidade
    return 1

"""
** Objetivo: atualizar unidades de um jogo no estoque
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Atualiza o dicionário estrutura com a quantiade correta
** Acoplamento
* Parâmetro:
- estrutura -> dict: estrutura que deve ter conteúdo impresso em totalidade
- nome -> string: nome do jogo que deve ter a quantidade atualizada
* Retornos:
- -4: caso de 'estrutura' não ser dict
- -5: caso de 'quantidade' não ser int ou 'nome' não ser string
- 1: em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor correto da quantidade
"""
@validaArg
def diminuir_quantidade(estrutura, nome, quantidade):
    if not isinstance(estrutura, dict):
        print("Erro, a estrutura passada não é dict")
        return -4
    if not isinstance(quantidade, int):
        print("Erro, a quantidade passada não é inteiro")
        return -5
    if not isinstance(nome, str):
        print("Erro, o nome não é uma string")
        return -5   
    
    if estrutura[nome] <= quantidade:
        if (estrutura[nome] < quantidade):
            print(f"Nao ha unidades suficientes, iremos retirar apenas {estrutura[nome]} unidades")
        print(f"Iremos repor em 10 unidades o jogo {nome} após o estoque ter zerado")
        estrutura[nome] = 10
    else:
        estrutura[nome] -= quantidade  
    
    return 1


"""
** Objetivo: inserir unidades de um jogo no estoque
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Atualiza o dicionário estrutura com a quantiade correta
** Acoplamento
* Parâmetro:
- estrutura -> dict: estrutura que deve ter conteúdo impresso em totalidade
- nome -> string: nome do jogo que deve ter a quantidade atualizada
* Retornos:
- -4: caso de 'estrutura' não ser dict
- -5: caso de 'quantidade' não ser int ou 'nome' não ser string
- 1: em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor correto da quantidade
"""
@validaArg
def aumentar_quantidade(estrutura, nome, quantidade=10):
    if not isinstance(estrutura, dict):
        print("Erro, a estrutura passada não é dict")
        return -4
    if not isinstance(quantidade, int):
        print("Erro, a quantidade passada não é inteiro")
        return -5
    if not isinstance(nome, str):
        print("Erro, o nome não é uma string")
        return -5
    if nome not in estrutura.keys():
        return 0
    estrutura[nome] += 10 # simples.retorna10()
    return 1

