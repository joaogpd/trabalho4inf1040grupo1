__all__ = ["alterar_nome", "alterar_preco"]

def alterar_nome(estrutura, nome, nome_novo):
  if nome not in estrutura.keys():
    return -1
  else:
    estrutura[nome_novo] = estrutura[nome]
    del estrutura[nome_novo]
    return 0
  
def alterar_preco(estrutura, nome, preco_novo):
  if nome not in estrutura.keys():
    return -1
  else:
    estrutura[nome] = preco_novo
    return 0
