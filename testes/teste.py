__all__ = ["teste_atualizacao_preco_e_nome"]


# mocking, deve ser chamada de outro módulo
def alterar_nome(estrutura, nome_atual, nome_novo):
  return

# mocking, deve ser chamada de outro módulo
def alterar_preco(estrutura, nome, preco_novo):
  return

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


#mocking
def remove_jogo():
    return

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


