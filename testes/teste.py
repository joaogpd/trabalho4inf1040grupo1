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
