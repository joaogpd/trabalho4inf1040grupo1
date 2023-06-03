__all__ = ["remove_jogo", "exibe_todos_estoque"]

def remove_jogo(nome, estrutura):
    if not isinstance(nome, str):
        return -1 #Nome invalido
    if nome in estrutura:
        del estrutura[nome]
        return 1 #Jogo removido com sucesso
    return 0 #Jogo nao encontrado (já removido)

def exibe_todos_estoque(estrutura):
  if not estrutura:
    return -1 # Estrutura vazia. Dicionario vazio "valued" como "false"
  for i in estrutura.keys():
    print("Nome: {}".format(i))
    return 0

def exibe_jogo(nome, estrutura):
    if not isinstance(nome,str):
        return -2 #Nome inválido
    if estrutura==0:
        print("Estrutura vazia")
        return -1 #Estrutura vazia
    if nome in estrutura:
        print("Nome: {}\nPreco: {}",format(nome,estrutura[nome]))
        return 0 #Jogo existente
    
