__all__ = ["remove_jogo", "exibe_todos_estoque"]

def remove_jogo(nome, estrutura):
    if not isinstance(nome, str):
        return -1 #Nome invalido
    if nome in estrutura:
        del estrutura[nome]
        return 1 #Jogo removido com sucesso
    return 0 #Jogo nao encontrado (já removido)

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
- msgerro1: caso de 'estrutura' não ser dict
- msgerro2: caso de 'estrutura' estar vazia
- msgsucesso: caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe um parâmetro
* Assertivas de saída:
- Todos as chaves da estrutura foram impressas
"""
def exibe_todos_estoque(estrutura):
  if not isinstance(estrutura, dict):
    return -2
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

def inserir_jogo(estrutura, nome, quantidade=10):
    
    #Tratando casos de parametros invalidos
    
    if not isinstance(estrutura, dict):
        print("Erro, a estrutura passada não é dict")
        return -4
    if not isinstance(quantidade, int):
        print("Erro, a quantidade passada não é inteira")
        return -5
    if not isinstance(nome, str):
        print("Erro, o nome não é uma string")
        return -5
    
    #tratando casos de parametros invalidos

    estrutura[nome] = quantidade
    return estrutura
