from catalogo/catalogo.py import *

__all__ = ["teste_atualizacao_preco_e_nome", "teste_remove_jogo", "teste_restaura_persiste"]

#### mocking, deve ser chamada de outro módulo ####

def restaura_estrutura(json):
    return

def recebe_pedidos(json):
    return

def persiste_estrutura(estrutura):
    return

def insere_jogo(nome, preco, estrutura):
    return

def remove_jogo(nome, estrutura):
    return

def exibe_todos(estrutura):
    return

def exibe_jogo(nome,estrutura):
    return

#### mocking, deve ser chamada de outro módulo ####


def teste_atualizacao_preco_e_nome():
  dados = dict()
  nome_nao_presente = "jogonaopresente"
  nome_presente = "jogovelho"
  nome_novo = "jogonovo"
  preco_novo = 12

  print("alterar_nome()")
  # Caso 1: nome de jogo nao presente
  execution_result = alterar_nome(dados, nome_nao_presente, "qualquer")
  if (execution_result == -1) and (nome_nao_presente not in dados.keys()):
    print("Passou no caso 1")
  else:
    print("Não passou no caso 1")
  # Confirmar mensagem de erro de jogo nao encontrado

  # Caso 2: nome de jogo presente
  alterar_nome(dados, nome_presente, nome_novo)
  if (execution_result == 0) and (nome_novo
                                  in dados.keys()) and (nome_presente
                                                        not in dados.keys()):
    print("Passou no caso 2")
  else:
    print("Não passou no caso 2")

  print("alterar_preco()")
  # Caso 1: preço de jogo nao presente
  execution_result = alterar_preco(dados, nome_nao_presente, 23)
  if execution_result == -1:
    print("Passou no caso 1")
  else:
    print("Não passou no caso 1")
  # Confirmar mensagem de erro de jogo nao encontrado

  # Caso 2: preço de jogo presente
  execution_result = alterar_preco(dados, nome_novo, preco_novo)
  if (execution_result == 0) and (nome_novo
                                  in dados.keys()) and (dados[nome_novo]
                                                        == preco_novo):
    print("Passou no caso 2")
  else:
    print("Não passou no caso 2")


def teste_remove_jogo():
    print("remove_jogo")
    #estrutura ficticia
    estrutura = {"nome1":0, "nome2":10, "nome3":21}
    nome_invalido = "nome0"
    nome_valido = "nome1"
    estruturaAux = estrutura

    #testando remoção de jogo invalido
    remove_jogo(nome_invalido, estrutura)
    if estrutura == estruturaAux:
        print("Passou no caso 1 (nome_nao_presente)")
    else:
        print("Não passou no caso 1 (nome_nao_presente)")
        return 1

    #testando remoção de jogo valido
    remove_jogo(nome_valido,estrutura)
    if nome_valido not in estrutura.keys():
        print("Passou no caso 3 (nome_presente)")
    else:
        print("Não passou no caso 3 (nome_presente)")
        return 1

    #testando remoção de jogo já removido
    estruturaAux = estrutura
    remove_jogo(nome_valido,estrutura)
    if estruturaAux == estrutura:
        print("Passou no caso 2 (nome_ja_removido)")
    else:
        print("Não passou no caso 2 (nome_ja_removido)")
        return 1

    return 0


def teste_restaura_persiste():
    print("restaura_persiste")

    #tad correto (dict)
    estrutura_valida = {"nome1": 10,
                        "nome2" : 20,
                        "nome3" : 30}
    
    #tad incorreto
    estrutura_invalida = [1,2,3]

    #nome de arquivo
    nome_valido = "dados_estrutura.json"
    nome_invalido = "blabla.js"

    persiste_estrutura(estrutura_valida)
    estrutura_retornada = restaura_estrutura(nome_valido)

    if estrutura_retornada == estrutura_valida:
        print("Passou no caso 1 (estrutura_valida, nome_valido)")
    else:
        print("Não passou no caso 1 (estrutura_valida, nome_valido)")
        return 1
    
    try: 
        restaura_estrutura(nome_invalido)
    except Exception as e:
        print(f"Não passou no caso 2 (nome_invalido) {type(e).__name__}")
        return 1
    else:
        print("Passou no caso 2 (nome_invalido)")

    try: 
        persiste_estrutura(estrutura_invalida)
    except Exception as e:
        print(f"Não passou no caso 3 (estrutura_invalida) {type(e).__name__}")
        return 1
    else:
        print("Passou no caso 3 (estrutura_invalida)")
    
    return 0

def teste_recebe_pedidos():
    print("recebe_pedidos()")

    pedido_valido = "pedido.json"
    pedido_invalido = "pedido.py"

    #Caso 1: arquivo vazio
    ret = recebe_pedidos(pedido_valido)
    if ret == 0:
        print("Passou no caso 1 (retornou o codigo de arquivo vazio)")
    else:
        print("Nao passou no caso 1")
        return 1

    #Caso 2: pedido invalido
    ret = recebe_pedidos(pedido_invalido)
    if ret == -1:
        print("Passou no caso 2 (retornou o codigo de arquivo invalido)")
    else:
        print("Nao passou no caso 2")
        return 1

    #Caso 3: pedido valido
    ret = recebe_pedidos(pedido_valido)
    if ret == 1:
        print("Passou no caso 3 (retornou o codigo de arquivo valido)")
    else:
        print("Nao passou no caso 3")
        return 1

    return 0

def teste_insere_jogo():

    print("insere_jogo()")

    #{nomeX: preco}
    estrutura = {"nome1":10,
                 "nome2":20,
                 "nome3":30}
    
    estrutura_somada = {"nome1":10,
                 "nome2":20,
                 "nome3":30,
                 "nome4":40}
    backup = estrutura

    nome_valido = "nome4"
    nome_invalido = 1990
    preco_valido = 40
    preco_invalido = "quarenta"

    #Caso 1: nome valido, preço valido
    insere_jogo(nome_valido, preco_valido, estrutura)
    if estrutura == estrutura_somada and ret == 1:
        print("Passou no caso 1")
    else:
        print("Nao passou no caso 1")
        return 1

    #Caso 2: nome valido, preço invalido
    #Funcao insere_jogo deve retonar codigo de erro para preco invalido (-2)
    ret = insere_jogo(nome_valido, preco_invalido, estrutura)
    if estrutura == backup and ret == -2:
        print("Passou no caso 2 (nao inseriu nada e retornou o codigo de erro)")
    else:
        print("Não passou no caso 2")
        return 1

    #Caso 3: nome invalido, preço valido
    #Funcao insere_jogo deve retonar codigo de erro para nome invalido (-1)
    ret = insere_jogo(nome_invalido, preco_valido, estrutura)
    if estrutura == backup and ret == -2:
        print("Passou no caso 3 (nao inseriu nada e retornou o codigo de erro)")
    else:
        print("Não passou no caso 3")
        return 1
    
    #Caso 4: nome inválido, preço inválido
    #Funcao insere_jogo deve retonar codigo de erro para nome e preco invalido (-3)
    ret = insere_jogo(nome_invalido, preco_invalido, estrutura)
    if estrutura == backup and ret == -3:
        print("Passou no caso 4 (nao inseriu nada e retornou o codigo de erro)")
    else:
        print("Não passou no caso 4")
        return 1

    #Caso 5: elemento já presente
    #Funcao insere_jogo deve retonar codigo de erro para nome já presente (0)
    ret = insere_jogo(nome_valido, preco_valido, estrutura)
    if estrutura == backup and ret == 0:
        print("Passou no caso 5 (nao inseriu nada e retornou o codigo de erro)")
    else:
        print("Não passou no caso 5")
        return 1

    return 0

def teste_exibe_todos():
    print("exibe_todos")

    #TAD correto
    estrutura_valida="preenchida"
    
    #TAD incorreto
    estrutura_invalida="vazia"

    #testando exibição com estrutura invalida
    resultado=exibe_todos(estrutura_invalida)
    
    if resultado == -1:
        print("Passou no caso 1 (estrutura vazia)")
        return 1
    else:
        print("Não passou no caso 1 (estrutura vazia)")

    #testando exibição com estrutura não vazia
    resultado=exibe_todos(estrutura_valida)

    if resultado == 0:
        print("Passou no caso 2 (estrutura não vazia)")
    else:
        print("Não passou no caso 2 (estrutura não vazia)")
        return 1
    
    return 0

def teste_exibe_jogo():
    print("exibe_jogo")
    #TAD correto
    estrutura_valida=dict()   
    #TAD incorreto
    estrutura_invalida="vazia"
    #nome valido
    nome_valido="nome do jogo"
    #nome invalido
    nome_invalido="nome da loja"
    #nome de jogo removido
    nome_removido="jogo removido"
    #nome de jogo inexistente
    nome_inexistente="jogo inexistente"

    #testando exibição com nome invalido
    resultado=exibe_jogo(nome_invalido,estrutura_valida)
    if resultado == -2:
        print("Passou no caso 1 (nome invalido)")
    else:
        print("Não passou no caso 1 (nome invalido)")
        return 1
    
    #testando exibição com estrutura vazia
    resultado=exibe_jogo(nome_valido,estrutura_invalida)

    if resultado == -1:
        print("Passou no caso 2 (estrutura vazia)")   
    else:
        print("Não passou no caso 2 (estrutura vazia)")
        return 1
    
    #testando exibição com jogo presente
    resultado=exibe_jogo(nome_valido,estrutura_valida)
    
    if resultado==0:
        print("Passou no caso 3 (jogo presente)")  
    else:
        print("Não passou no caso 3 (jogo presente)") 
        return 1

    #testando exibição com jogo não presente
    resultado=exibe_jogo(nome_removido,estrutura_valida)
    
    if resultado==1:
        print("Passou no caso 4 (jogo anteriormente removido)")  
    else:
        print("Não passou no caso 4 (jogo anteriormente removido)") 
        return 1

    #testando exibição com jogo nunca existente
    resultado=exibe_jogo(nome_inexistente,estrutura_valida)
    
    if resultado==2:
        print("Passou no caso 4 (jogo nunca existente)")  
    else:
        print("Não passou no caso 4 (jogo nunca existente)") 
        return 1
    return 0
