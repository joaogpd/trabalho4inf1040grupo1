__all__ = ["alterar_nome", "alterar_preco", "exibe_todos_catalogo", "cadastrar"]

"""
** Objetivo: trocar o nome de um jogo do catálogo por um novo
** Descrição detalhada:
- Valida os tipos dos parâmetros recebidos
- Confere se o 'nome' passado encontra-se na 'estrutura' recebida
- Adiciona uma entrada com o 'nome_novo' com o conteúdo de 'nome'
- Remove 'nome' da 'estrutura'
** Acoplamento
* Parâmetros:
- estrutura -> dict: estrutura que contém o nome a ser atualizado pela função
- nome -> string: nome atual que deve ser alterado
- nome_novo -> string: nome novo para o qual o antigo deve ser alterado 
* Retornos:
- -10: caso de 'estrutura' não ser dict
- -11: caso de 'nome' não ser str
- -11: caso de 'nome_novo' não ser str
- -12: caso de 'nome' não presente na 'estrutura'
- 1: caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função deve receber três parâmetros
* Assertivas de saída:
- O nome antigo ('nome') deve ter sido removido da estrutura
- O nome novo ('nome_novo') deve estar presente com o conteúdo do antigo
"""
def alterar_nome(estrutura, nome, nome_novo):
  if not isinstance(estrutura, dict):
    return -10
  if not isinstance(nome, str):
    return -11
  if not isinstance(nome_novo, str):
    return -11
  if nome not in estrutura.keys():
    return -12
  else:
    estrutura[nome_novo] = estrutura[nome]
    del estrutura[nome_novo]
    return 1
  
"""
** Objetivo: alterar o preço de uma entrada na estrutura
** Descrição detalhada:
- Valida os tipos dos parâmetros recebidos
- Confere se o 'nome' passado encontra-se na 'estrutura' recebida
- Altera o valor de 'nome' na estrutura para 'preco_novo'
** Acoplamento
* Parâmetros:
- estrutura -> dict: estrutura que contém o nome a ter valor atualizado pela função
- nome -> string: nome atual que contém o valor que deve ser alterado
- preco_novo -> int, float: preço novo para o qual a chave deve ser atualizada
* Retornos:
- msgerro2: caso de 'estrutura' não ser dict
- msgerro3: caso de 'nome' não ser str
- msgerro4: caso de 'preco_novo' não ser int ou float
- msgerro1: caso de 'nome' não presente na 'estrutura'
- msgsucesso: caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função deve receber três parâmetros
* Assertivas de saída:
- O nome ('nome') deve ter conteúdo igual ao preço novo passado na função ('preco_novo')
"""
def alterar_preco(estrutura, nome, preco_novo):
  if not isinstance(estrutura, dict):
    return -13
  if not isinstance(nome, str):
    return -14
  if not (isinstance(preco_novo, int) or isinstance(preco_novo, float)):
    return -15
  if nome not in estrutura.keys():
    return -12
  else:
    estrutura[nome] = preco_novo
    return 1

"""
** Objetivo: exibir todos os itens da estrutura catálogo
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
- Confere se a estrutura está vazia
- Imprime todos os valores presentes na estrutura
** Acoplamento
* Parâmetro:
- estrutura -> dict: estrutura que deve ter conteúdo impresso em totalidade
* Retornos:
- -8: caso de 'estrutura' não ser dict
- -9: caso de 'estrutura' estar vazia
- 1: caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe um parâmetro
* Assertivas de saída:
- Todos os conteúdos da estrutura foram impressos
"""
def exibe_todos_catalogo(estrutura):
  if not isinstance(estrutura, dict):
    return -8
  if not estrutura:
    return -9
  for i in estrutura.keys():
    print("Nome: {} Preço: {}".format(i, estrutura[i]))
  return 1


"""
** Objetivo: cadastrar um novo jogo no catalogo
** Descrição detalhada:
- Valida o tipo do parâmetro recebido
** Acoplamento
* Parâmetro:
- estrutura -> dict: estrutura que deve ter conteúdo impresso em totalidade
* Retornos:
- msgerro1: caso de 'estrutura' não ser dict
- msgerro2: caso de 'preco' não ser int nem float ou 'nome' não ser string
- estrutura em caso de sucesso
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
* Assertivas de saída:
- O jogo de nome 'nome' deve estar na estrutura com o valor preco
"""
def cadastrar(estrutura, nome, preco):
    
    # Tratando casos de parametros invalidos
    
    if not isinstance(estrutura, dict):
        print("Erro, a estrutura passada não é dict")
        return -4
    if not (isinstance(preco, int) or isinstance(preco, float)):
        print("Erro, o preco passado não é inteiro nem float")
        return -5
    if not isinstance(nome, str):
        print("Erro, o nome não é uma string")
        return -5
    
    # tratando casos de parametros invalidos
    

    estrutura[nome] = preco
    return 1
