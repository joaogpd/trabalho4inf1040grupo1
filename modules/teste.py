from catalogo.catalogo import *
from estoque.estoque import *
#from tratamentojson.tratamentojson import *

def teste_atualizacao_preco_e_nome():
  dados = dict()
  nome_nao_presente = "jogonaopresente"
  nome_presente = "jogovelho"
  nome_novo = "jogonovo"
  preco_novo = 12

  dados[nome_presente] = 10

  print("alterar_nome()")
  # Caso 1: nome de jogo nao presente
  execution_result = alterar_nome(dados, nome_nao_presente, "qualquer")
  if execution_result == -12:
    print("Passou no caso 1 (nome de jogo não presente)")
  else:
    print("Não passou no caso 1 (nome de jogo não presente)")
  # Confirmar mensagem de erro de jogo nao encontrado

  # Caso 2: nome de jogo presente
  execution_result = alterar_nome(dados, nome_presente, nome_novo)
  if execution_result == 1:
    print("Passou no caso 2 (nome de jogo presente)")
  else:
    print("Não passou no caso 2 (nome de jogo presente)")

  # Caso 3: estrutura não é dict
  execution_result = alterar_nome("abc", nome_presente, nome_novo)
  if execution_result == -10:
    print("Passou no caso 3 (estrutura não é dict)")
  else:
    print("Não passou no caso 3 (estrutura não é dict)")

  # Caso 4: nome não é str
  execution_result = alterar_nome(dados, 10, nome_novo)
  if execution_result == -11:
    print("Passou no caso 4 (nome não é str)")
  else:
    print("Não passou no caso 4 (nome não é str)")

  # Caso 5: nome_novo não é str
  execution_result = alterar_nome(dados, nome_presente, 5)
  if execution_result == -11:
    print("Passou no caso 5 (nome_novo não é str)")
  else:
    print("Não passou no caso 5 (nome_novo não é str)")

  print("alterar_preco()")
  # Caso 1: preço de jogo nao presente
  execution_result = alterar_preco(dados, nome_nao_presente, 23)
  if execution_result == -12:
    print("Passou no caso 1 (preço de jogo não presente)")
  else:
    print("Não passou no caso 1 (preço de jogo não presente)")
  # Confirmar mensagem de erro de jogo nao encontrado

  # Caso 2: preço de jogo presente
  execution_result = alterar_preco(dados, nome_novo, preco_novo)
  if execution_result == 1:
    print("Passou no caso 2 (preço de jogo presente)")
  else:
    print("Não passou no caso 2 (preço de jogo presente)")

  # Caso 3: estrutura não é dict
  execution_result = alterar_preco("abc", nome_presente, preco_novo)
  if execution_result == -13:
    print("Passou no caso 3 (estrutura não é dict)")
  else:
    print("Não passou no caso 3 (estrutura não é dict)")

  # Caso 4: nome não é str
  execution_result = alterar_preco(dados, 10, preco_novo)
  if execution_result == -14:
    print("Passou no caso 4 (nome não é str)")
  else:
    print("Não passou no caso 4 (nome não é str)")

  # Caso 5: preco_novo não é numeric
  execution_result = alterar_preco(dados, nome_presente, "abc")
  if execution_result == -15:
    print("Passou no caso 5 (preco_novo não é str)")
  else:
    print("Não passou no caso 5 (preco_novo não é str)")


def teste_remove_jogo():
    print("remove_jogo")
    # estrutura ficticia
    estrutura = {"nome1": 0, "nome2": 10, "nome3": 21}
    nome_invalido = "nome0"
    nome_valido = "nome1"
    estruturaAux = estrutura

    # testando remoção de jogo invalido
    execution_result = remove_jogo(nome_invalido, estrutura)
    if execution_result == 0:
        print("Passou no caso 1 (nome_nao_presente)")
    else:
        print("Não passou no caso 1 (nome_nao_presente)")

    # testando remoção de jogo valido
    execution_result = remove_jogo(nome_valido, estrutura)
    if execution_result == 1:
        print("Passou no caso 2 (nome_presente)")
    else:
        print("Não passou no caso 2 (nome_presente)")

    # testando remoção de jogo já removido
    estruturaAux = estrutura
    execution_result = remove_jogo(nome_valido, estrutura)
    if execution_result == 0:
        print("Passou no caso 3 (nome_ja_removido)")
    else:
        print("Não passou no caso 3 (nome_ja_removido)")

    # caso de nome não ser str
    execution_result = remove_jogo(10, estrutura)
    if execution_result == -1:
        print("Passou no caso 4 (nome_nao_str)")
    else:
        print("Não passou no caso 4 (nome_nao_str)")


def teste_restaura_persiste():
    print("restaura_persiste")

    # tad correto (dict)
    estrutura_valida = {"nome1": 10,
                        "nome2" : 20,
                        "nome3" : 30}
    
    # tad incorreto
    estrutura_invalida = [1,2,3]

    # nome de arquivo
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

    print("inserir_jogo()")

    #{nomeX: quantidade}
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

    # Caso 1: nome valido, quantidade válida
    execution_result = inserir_jogo(estrutura, nome_valido, preco_valido)
    if execution_result == 1:
        print("Passou no caso 1 (parâmetros válidos)")
    else:
        print("Nao passou no caso 1 (parâmetros válidos)")

    # Caso 2: nome valido, quantidade inválida
    # Funcao insere_jogo deve retornar codigo de erro para preco invalido (-5)
    execution_result = inserir_jogo(estrutura, nome_valido, preco_invalido)
    if execution_result == -5:
        print("Passou no caso 2 (quantidade inválida)")
    else:
        print("Não passou no caso 2 (quantidade inválida)")

    # Caso 3: nome invalido, quantidade válida
    # Funcao insere_jogo deve retonar codigo de erro para nome invalido (-5)
    execution_result = inserir_jogo(estrutura, nome_invalido, preco_valido)
    if execution_result == -5:
        print("Passou no caso 3 (nome inválido)")
    else:
        print("Não passou no caso 3 (nome inválido)")

    # Caso 4: estrutura inválida
    execution_result = inserir_jogo("", nome_valido, preco_valido)
    if execution_result == -4:
        print("Passou no caso 4 (estrutura inválida)")
    else:
        print("Não passou no caso 4 (estrutura inválida)")

    # Avaliar impacto na geração de log

    # # Caso 5: elemento já presente
    # # Funcao insere_jogo deve retonar codigo de erro para nome já presente (0)
    # execution_result = inserir_jogo(nome_valido, preco_valido, estrutura)
    # if estrutura == backup and ret == 0:
    #     print("Passou no caso 5 (nao inseriu nada e retornou o codigo de erro)")
    # else:
    #     print("Não passou no caso 5")

def teste_exibe_todos():
    print("exibe_todos")

    #TAD correto
    estrutura_valida = {"nome1":10,"nome2":20,"nome3":30}
    
    #TAD incorreto
    estrutura_invalida = {}

    #testando exibição com estrutura invalida
    resultado = exibe_todos_estoque(estrutura_invalida)
    
    if resultado == -1:
        print("Passou no caso 1 (estrutura vazia)")
        return 1
    else:
        print("Não passou no caso 1 (estrutura vazia)")

    #testando exibição com estrutura não vazia
    resultado = exibe_todos(estrutura_valida)

    if resultado == 0:
        print("Passou no caso 2 (estrutura não vazia)")
    else:
        print("Não passou no caso 2 (estrutura não vazia)")
        return 1
    
    return 0

def teste_exibe_jogo():
    print("exibe_jogo")
    #TAD correto
    estrutura_valida={"nome1":10,"nome2":20,"nome3":30}
    #TAD incorreto
    estrutura_invalida={}
    #nome valido
    nome_valido="Detetive"
    #nome invalido
    nome_invalido=3
    #nome de jogo removido
    nome_removido="Jogo da Vida"
    #nome de jogo inexistente
    nome_inexistente="WAR"

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
    resultado=remove_jogo(nome_removido,estrutura_valida)
    
    if resultado==1:
        print("Passou no caso 4 (jogo anteriormente removido)")  
    else:
        print("Não passou no caso 4 (jogo anteriormente removido)") 
        return 1

    #testando exibição com jogo nunca existente
    resultado=remove_jogo(nome_inexistente,estrutura_valida)
    
    if resultado==1:
        print("Passou no caso 4 (jogo nunca existente)")  
    else:
        print("Não passou no caso 4 (jogo nunca existente)") 
        return 1
    return 0

def teste_gera_log():
    print("gera_log")

    arg_valido = {"blabla": "bla"}
    arg_invalido = [1,2,3,4]
    if gera_log(arg_valido) != 0:
        print("Não passou no caso 1 (estrutura valida")
        return 1
    if gera_log(arg_invalido) >= 0:
        print("Não passou no caso 2 (estrutura invalida)")
        return 1
    print("Passou nos casos 1 e 2")
    return 0

def main_teste():
    teste_atualizacao_preco_e_nome()
    teste_remove_jogo()
    # teste_restaura_persiste()
    # teste_recebe_pedidos()
    teste_insere_jogo()
    # teste_exibe_todos()
    # teste_exibe_jogo()
    # teste_gera_log()
    print("TESTING DONE")


if __name__ == '__main__':
    main_teste()
