__all__ = ["remove_jogo", "exibe_todos_estoque", "exibe_jogo", "inserir_jogo", "diminuir_quantidade", "aumentar_quantidade"]

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
        return -2 # Nome inválido
    if estrutura==0:
        print("Estrutura vazia")
        return -1 #Estrutura vazia
    if nome in estrutura:
        print("Nome: {}\nPreco: {}", format(nome, estrutura[nome]))
        return 0 # Jogo existente

    
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
- msgerro1: caso de 'estrutura' não ser dict
- msgerro2: caso de 'quantidade' não ser int ou 'nome' não ser string
- estrutura em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor correto da quantidade
"""
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
    
    # tratando casos de parametros invalidos

    estrutura[nome] = quantidade
    return estrutura

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
- msgerro1: caso de 'estrutura' não ser dict
- msgerro2: caso de 'quantidade' não ser int ou 'nome' não ser string
- estrutura em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor correto da quantidade
"""
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
    
    return estrutura


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
- msgerro1: caso de 'estrutura' não ser dict
- msgerro2: caso de 'quantidade' não ser int ou 'nome' não ser string
- estrutura em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor correto da quantidade
"""
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
    estrutura[nome] += quantidade
    return estrutura

