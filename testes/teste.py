__all__ = ["teste_atualizacao_preco_e_nome", "teste_remove_jogo", "teste_restaura_persiste"]


#### mocking, deve ser chamada de outro módulo ####

def alterar_nome(estrutura, nome_atual, nome_novo):
  return

def alterar_preco(estrutura, nome, preco_novo):
  return

def restaura_estrutura(json):
    return

def persiste_estrutura(estrutura):
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
