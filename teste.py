from modules.catalogo.catalogo import *
from modules.estoque.estoque import *
from modules.tratamentojson.tratamentojson import *

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
    estrutura_valida_estoque = {"nome1" : 10, "nome2" : 20, "nome3" : 15}
    estrutura_valida_catalogo = {"nome1" : 2.0, "nome2" : 3.2, "nome3" : 5.6}
    
    print("persiste_estrutura()")

    # Caso 1: estoque ou catalogo inválidos
    execution_result = persiste_estrutura("", "")
    if execution_result == -8:
        print("Passou no caso 1 (estoque ou catalogo invalidos)")
    else:
        print("Não passou no caso 1 (estoque ou catalogo inválidos)")

    # Caso 2: sucesso
    execution_result = persiste_estrutura(estrutura_valida_estoque, estrutura_valida_catalogo)
    if execution_result == 1:
        print("Passou no caso 2 (sucesso)")
    else:
        print("Não passou no caso 2 (sucesso)")

    print("restaura_estrutura_estoque()")

    estrutura_vazia = dict()

    # Caso 1: arquivo vazio
    execution_result = restaura_estrutura_estoque("vazio.json", estrutura_vazia)
    if execution_result == -18:
        print("Passou no caso 1 (arquivo vazio)")
    else:
        print("Não passou no caso 1 (arquivo vazio)")
    
    # Caso 2: arquivo inválido
    execution_result = restaura_estrutura_estoque("invalid.txt", estrutura_vazia)
    if execution_result == -18:
        print("Passou no caso 2 (arquivo inválido)")
    else:
        print("Não passou no caso 2 (arquivo inválido)")

    # Caso 3: execução com sucesso
    execution_result = restaura_estrutura_estoque("estrutura.json", estrutura_vazia)
    if execution_result == 1:
        print("Passou no caso 3 (execução com sucesso)")
    else:
        print("Não passou no caso 3 (execução com sucesso)")

    print("restaura_estrutura_catalogo()")
    
     # Caso 1: arquivo vazio
    execution_result = restaura_estrutura_catalogo("vazio.json", estrutura_vazia)
    if execution_result == -18:
        print("Passou no caso 1 (arquivo vazio)")
    else:
        print("Não passou no caso 1 (arquivo vazio)")
    
    # Caso 2: arquivo inválido
    execution_result = restaura_estrutura_catalogo("invalid.txt", estrutura_vazia)
    if execution_result == -18:
        print("Passou no caso 2 (arquivo inválido)")
    else:
        print("Não passou no caso 2 (arquivo inválido)")

    # Caso 3: execução com sucesso
    execution_result = restaura_estrutura_catalogo("estrutura.json", estrutura_vazia)
    if execution_result == 1:
        print("Passou no caso 3 (execução com sucesso)")
    else:
        print("Não passou no caso 3 (execução com sucesso)")

def teste_recebe_pedidos():
    print("recebe_pedidos()")

    pedido_valido = "pedidoteste1.json"
    pedido_vazio = "vazio.json"
    pedido_invalido = "steinsgate"
    estrutura_valida_estoque = {
        "nome1": 10,
        "nome2" : 20,
        "nome3" : 30
    }

    #Caso 1: arquivo vazio
    try:
        tratar_solicitacao_compra(pedido_vazio, estrutura_valida_estoque)
    except:
        print("Não passou no caso 1 (pedidio vazio)")
    print("Passou no caso 1 (pedido vazio)")

    #Caso 2: pedido invalido
    try:
        tratar_solicitacao_compra(pedido_invalido,estrutura_valida_estoque)
    except:
        print("Não passou no caso 2 (pedidio invalido)")
    print("Passou no caso 2 (pedido invalido)")

    #Caso 3: pedido valido
    try:
        tratar_solicitacao_compra(pedido_valido,estrutura_valida_estoque)
    except:
        print("Não passou no caso 3 (pedidio valido)")
    print("Passou no caso 3 (pedido valido)")

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
    quantidade_valida = 40
    quantidade_invalida = "quarenta"

    # Caso 1: nome valido, quantidade válida
    execution_result = inserir_jogo(estrutura, nome_valido, quantidade_valida)
    if execution_result == 1:
        print("Passou no caso 1 (parâmetros válidos)")
    else:
        print("Nao passou no caso 1 (parâmetros válidos)")

    # Caso 2: nome valido, quantidade inválida
    # Funcao insere_jogo deve retornar codigo de erro para preco invalido (-5)
    execution_result = inserir_jogo(estrutura, nome_valido, quantidade_invalida)
    if execution_result == -5:
        print("Passou no caso 2 (quantidade inválida)")
    else:
        print("Não passou no caso 2 (quantidade inválida)")

    # Caso 3: nome invalido, quantidade válida
    # Funcao insere_jogo deve retonar codigo de erro para nome invalido (-5)
    execution_result = inserir_jogo(estrutura, nome_invalido, quantidade_valida)
    if execution_result == -5:
        print("Passou no caso 3 (nome inválido)")
    else:
        print("Não passou no caso 3 (nome inválido)")

    # Caso 4: estrutura inválida
    execution_result = inserir_jogo("", nome_valido, quantidade_valida)
    if execution_result == -4:
        print("Passou no caso 4 (estrutura inválida)")
    else:
        print("Não passou no caso 4 (estrutura inválida)")

def teste_cadastrar():

    print("cadastrar()")

    #{nomeX: preco}
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

    # Caso 1: nome valido, preco válido
    execution_result = cadastrar(estrutura, nome_valido, preco_valido)
    if execution_result == 1:
        print("Passou no caso 1 (parâmetros válidos)")
    else:
        print("Nao passou no caso 1 (parâmetros válidos)")

    # Caso 2: nome valido, preco inválido
    # Funcao cadastrar deve retornar codigo de erro para preco invalido (-5)
    execution_result = cadastrar(estrutura, nome_valido, preco_invalido)
    if execution_result == -5:
        print("Passou no caso 2 (preço inválido)")
    else:
        print("Não passou no caso 2 (preço inválido)")

    # Caso 3: nome invalido, preco válido
    # Funcao insere_jogo deve retonar codigo de erro para nome invalido (-5)
    execution_result = cadastrar(estrutura, nome_invalido, preco_valido)
    if execution_result == -5:
        print("Passou no caso 3 (nome inválido)")
    else:
        print("Não passou no caso 3 (nome inválido)")

    # Caso 4: estrutura inválida
    execution_result = cadastrar("", nome_valido, preco_valido)
    if execution_result == -4:
        print("Passou no caso 4 (estrutura inválida)")
    else:
        print("Não passou no caso 4 (estrutura inválida)")

def teste_exibe_todos():
    print("exibe_todos_catalogo()")

    # TAD correto
    estrutura_valida = {"nome1":10,"nome2":20,"nome3":30}
    
    # TAD incorreto
    estrutura_invalida = {}

    # Caso 1: estrutura não é dict
    execution_result = exibe_todos_estoque("")
    if execution_result == -8:
        print("Passou no caso 1 (estrutura não é dict)")
    else:
        print("Não passou no caso 1 (estrutura não é dict)")

    # Caso 2: estrutura válida
    execution_result = exibe_todos_estoque(estrutura_valida)
    if execution_result == 1:
        print("Passou no caso 2 (estrutura válida)")
    else:
        print("Não passou no caso 2 (estrutura válida)")

    # Caso 3: estrutura vazia
    execution_result = exibe_todos_estoque(estrutura_invalida)
    if execution_result == -9:
        print("Passou no caso 3 (estrutura vazia)")
    else:
        print("Não passou no caso 3 (estrutura vazia)")

    print("exibe_todos_catalogo()")

    # Caso 1: estrutura não é dict
    execution_result = exibe_todos_catalogo("")
    if execution_result == -8:
        print("Passou no caso 1 (estrutura não é dict)")
    else:
        print("Não passou no caso 1 (estrutura não é dict)")

    # Caso 2: estrutura válida
    execution_result = exibe_todos_catalogo(estrutura_valida)
    if execution_result == 1:
        print("Passou no caso 2 (estrutura válida)")
    else:
        print("Não passou no caso 2 (estrutura válida)")

    # Caso 3: estrutura vazia
    execution_result = exibe_todos_catalogo(estrutura_invalida)
    if execution_result == -9:
        print("Passou no caso 3 (estrutura vazia)")
    else:
        print("Não passou no caso 3 (estrutura vazia)")

def teste_exibe_jogo():
    print("exibe_jogo()")
    # TAD correto
    estrutura_valida = {"nome1":10, "nome2":20, "nome3":30}
    # TAD incorreto 
    estrutura_invalida = {}
    # nome valido
    nome_valido = "nome1"
    # nome invalido
    nome_invalido = 3
    # nome de jogo removido
    nome_removido = "Jogo da Vida"
    # nome de jogo inexistente
    nome_inexistente = "WAR"

    # testando exibição com nome invalido
    execution_result = exibe_jogo(nome_invalido,estrutura_valida)
    if execution_result == -11:
        print("Passou no caso 1 (nome invalido)")
    else:
        print("Não passou no caso 1 (nome invalido)")
    
    # testando exibição com estrutura vazia
    execution_result = exibe_jogo(nome_valido, estrutura_invalida)

    if execution_result == -9:
        print("Passou no caso 2 (estrutura vazia)")   
    else:
        print("Não passou no caso 2 (estrutura vazia)")
        return 1
    
    # testando exibição com jogo presente
    execution_result = exibe_jogo(nome_valido, estrutura_valida)
    
    if execution_result == 1:
        print("Passou no caso 3 (jogo presente)")  
    else:
        print("Não passou no caso 3 (jogo presente)") 

    # testando exibição com jogo não presente
    execution_result = remove_jogo(nome_removido,estrutura_valida)
    
    if execution_result == 0:
        print("Passou no caso 4 (jogo não presente)")  
    else:
        print("Não passou no caso 4 (jogo não presente)") 

def teste_alterar_quantidade():
    estrutura_valida = {"nome1":10, "nome2":20, "nome3":30}

    print("diminuir_quantidade()")
    # Caso 1: estrutura não é dict
    execution_result = diminuir_quantidade("", "nome2", 1)
    if execution_result == -4:
        print("Passou no caso 1 (estrutura não é dict)")
    else:
        print("Não passou no caso 1 (estrutura não é dict)")
    
    # Caso 2: quantidade não é int
    execution_result = diminuir_quantidade(estrutura_valida, "nome2", "1")
    if execution_result == -5:
        print("Passou no caso 2 (quantidade não é int)")
    else:
        print("Não passou no caso 2 (quantidade não é int)")

    # Caso 3: nome não é str
    execution_result = diminuir_quantidade(estrutura_valida, 3, 1)
    if execution_result == -5:
        print("Passou no caso 3 (nome não é str)")
    else:
        print("Não passou no caso 3 (nome não é str)")

    # Caso 4: sucesso
    execution_result = diminuir_quantidade(estrutura_valida, "nome2", 10)
    if execution_result == 1:
        print("Passou no caso 4 (sucesso)")
    else:
        print("Não passou no caso 4 (sucesso)")
    
    print("aumentar_quantidade()")
    # Caso 1: estrutura não é dict
    execution_result = aumentar_quantidade("", "nome2", 1)
    if execution_result == -4:
        print("Passou no caso 1 (estrutura não é dict)")
    else:
        print("Não passou no caso 1 (estrutura não é dict)")
    
    # Caso 2: quantidade não é int
    execution_result = aumentar_quantidade(estrutura_valida, "nome2", "1")
    if execution_result == -5:
        print("Passou no caso 2 (quantidade não é int)")
    else:
        print("Não passou no caso 2 (quantidade não é int)")

    # Caso 3: nome não é str
    execution_result = aumentar_quantidade(estrutura_valida, 3, 1)
    if execution_result == -5:
        print("Passou no caso 3 (nome não é str)")
    else:
        print("Não passou no caso 3 (nome não é str)")

    # Caso 4: nome não presente na estrutura
    execution_result = aumentar_quantidade(estrutura_valida, "abc", 1)
    if execution_result == 0:
        print("Passou no caso 4 (nome não presente)")
    else:
        print("Não passou no caso 4 (nome não presente)")

    # Caso 5: sucesso
    execution_result = diminuir_quantidade(estrutura_valida, "nome2", 10)
    if execution_result == 1:
        print("Passou no caso 5 (sucesso)")
    else:
        print("Não passou no caso 5 (sucesso)")

def teste_gera_log():
    print("gera_log()")

    arg_valido = {"blabla": "bla"}
    arg_invalido = [1,2,3,4]
    # Caso 1: parâmetro não é dict
    execution_result = gera_log(arg_invalido)
    if execution_result == -4:
        print("Passou no caso 1 (parâmetro não é dict)")
    else:
        print("Não passou no caso 1 (parâmetro não é dict)")

    # Caso 2: sucesso
    execution_result = gera_log(arg_valido)
    if execution_result == 1:
        print("Passou no caso 2 (sucesso)")
    else:
        print("Não passou no caso 2 (sucesso)")

def main_teste():
    teste_atualizacao_preco_e_nome()
    teste_remove_jogo()
    teste_restaura_persiste()
    # teste_recebe_pedidos()
    teste_insere_jogo()
    teste_cadastrar()
    teste_exibe_todos()
    teste_exibe_jogo()
    teste_alterar_quantidade()
    teste_gera_log()
    print("TESTING DONE")


if __name__ == '__main__':
    main_teste()
