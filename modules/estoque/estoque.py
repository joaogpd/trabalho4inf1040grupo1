def remove_jogo(nome, estrutura):
    if not isinstance(nome, str):
        return -1 #Nome invalido
    if nome in estrutura:
        del estrutura[nome]
        return 1 #Jogo removido com sucesso
    return 0 #Jogo nao encontrado (já removido)
