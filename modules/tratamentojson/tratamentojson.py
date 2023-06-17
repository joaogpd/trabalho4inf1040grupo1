from modules.catalogo.catalogo import *
from modules.estoque.estoque import *
import json

__all__ = ["tratar_pedidos_novojogo", "tratar_solicitacao_compra", "restaura_estrutura_estoque", "restaura_estrutura_catalogo", "persiste_estrutura"]

def validaArg(func):
    def wrapper(*args, **kwargs):
        if len(args) < 1:
            print(f"Error, função {func.__name__} não recebeu argumentos")
        return func(*args, **kwargs)
    return wrapper

"""
** Objetivo: Receber a solicitação de novos jogos
** Descrição detalhada:
- Valida o json recebido
- Adiciona  o jogo em questão ao catálogo e ao estoque
- 
** Acoplamento
* Parâmetro:
- solicitacao -> nome do arquivo json:
- estoque -> dict: estrutura que deve ter nome e quantidade de cada jogo
- catalogo -> dict: estrutura que deve ter nome e valor de cada jogo
* Retornos:
-  0 # Sucesso
- -1 # Jogo já pertencente ao catálogo
- -2 # Arquivo vazio
- -3 # Arquivo invalido
** Condições de acoplamento:
* Assertivas de entrada:
- Se o arquivo json estiver preenchido, foi de maneira correta
- funções auxiliares de verificar_json, cadastrar e aumentar_quantidade devem funcionar corretamente
* Assertivas de saída:
- Retorno de acordo com o resultado das operações internas
"""     
"""
Estrutura do arquivo json utilizado:
Em "estoque", "nome" : "quantidade"
Em "catalogo", "nome" : "preco"
{
    "estoque" : {
        "jogo_um" : 4,
        "jogo_dois" : 1,
        ...
    },
    "catalogo" : {
        "jogo_um" : 7.2,
        "jogo_dois" : 8.6,
        ...
    }
"""
@validaArg
def tratar_pedidos_novojogo(solicitacao,estoque,catalogo):
    #Recebimento do pedido
    if verificar_json(solicitacao) == -2:
        print("Arquivo de solicitacao .json está vazio")
        return -2 #Arquivo vazio
    
    elif verificar_json(solicitacao) == -3:
        print("Arquivo de solicitacao é invalido")
        return -3 #Arquivo invalido

    #Tratamento do pedido
    with open(solicitacao) as file:
        dados = json.load(file)

    for jogo in dados['jogos']:
        nome_jogo = jogo['nome']

        if nome_jogo not in catalogo:
            valor_jogo=input("Digite o valor do jogo {}:",format(nome_jogo))
            cadastrar(catalogo,nome_jogo,valor_jogo) # Adiciona no catalogo o jogo
            aumentar_quantidade(estoque, nome_jogo)  # Compra 10 unidades
            return 0
        else:
            print("Jogo já existente no catálogo")#jogo já cadastrado
            return -1
    

"""
** Objetivo: Tratar a solicitacao (arquivo json) de compra de jogos
** Descrição detalhada:
- Valida o arquivo recebido
- Faz a movimentacao de compra e venda necessaria
- Retorna o codigo equivalente ao resultado das movimentacoes
** Acoplamento
* Parâmetro:
- solicitacao -> nome do arquivo json: 
- estoque -> dict: estrutura que deve ter nome e quantidade de cada jogo
* Retornos:
-  1 # Sucesso
- -2 # Arquivo vazio
- -3 # Arquivo invalido
- -5 # 1+ quantidade insuficiente
- -6 # 1+ jogos sem cadastro
- -7 # 1+ jogos sem cadastro e/ou quantidade insuficiente
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 2 parâmetros
- Precisa das funcoew auxiliares, verificar_json, aumentar_quantidade e diminuir_quantidade
* Assertivas de saída:
- Realiza as operacoes (compra/venda) necessaria e retorna o codigo correspondente
- Arquivo de solicitacao JSON será descartado, entao nao é preciso fazer nada com ele
"""

# Solicitacao considerada:
# solicitacao.json =
# {
#   "jogos": [
#         {"nome": "Jogo1", "quantidade": 2},
#         {"nome": "Jogo2", "quantidade": 1},
#         {"nome": "Jogo3", "quantidade": 4}
#     ]
# }
#
# Estrutura considerada:
# estoque = {
#     "Jogo1": 3,
#     "Jogo2": 0,
#     "Jogo3": 2
# }

@validaArg
def tratar_solicitacao_compra(solicitacao, estoque):

    erro_quantidade = 0
    erro_cadastro = 0

    #Verifica o arquivo de solicitacao
    if verificar_json(solicitacao) == -2:
        print("Arquivo de solicitacao .json está vazio")
        return -2 #Arquivo vazio
    
    elif verificar_json(solicitacao) == -3:
        print("Arquivo de solicitacao é invalido")
        return -3 #Arquivo invalido

    # Carrega o .JSON
    with open(solicitacao) as file:
        dados = json.load(file)

    print('--')
    for jogo in dados['jogos']:
        nome_jogo = jogo['nome']
        quantidade_solicitada = jogo['quantidade']

        if nome_jogo in estoque:  # Jogo está cadastrado no sistema
            quantidade_disponivel = estoque[nome_jogo]
            if quantidade_disponivel == 0:
                print(f"O jogo {nome_jogo} esta em falta")

                # Repoe o estoque
                aumentar_quantidade(estoque, nome_jogo)  # Compra 10 unidades
                
                print(f"Um pedido de compra do jogo {nome_jogo} foi realizado")
                erro_quantidade+=1

            elif quantidade_disponivel < quantidade_solicitada:
                print(f"O jogo {nome_jogo} possui quantidade insuficiente em estoque")
                print(f"Quantidade disponível: {quantidade_disponivel}")
                print(f"Quantidade solicitada: {quantidade_solicitada}")

                # Repoe o estoque
                diminuir_quantidade(estoque, nome_jogo, quantidade_disponivel) # Remove/Vende todas unidades restantes
                aumentar_quantidade(estoque, nome_jogo)  # Compra 10 unidades
              
                print(f"Foram compradas apenas {quantidade_disponivel} unidades do jogo {nome_jogo}, e um pedido de reposicao do estoque foi realizado")
                erro_quantidade+=1

            elif quantidade_disponivel == quantidade_solicitada:
                diminuir_quantidade(estoque, nome_jogo, quantidade_solicitada) # Remove/Vende todas unidades solicitadas
                
                print(f"O jogo {nome_jogo} foi comprado com sucesso")
                print(f"Quantidade restante: {quantidade_disponivel - quantidade_solicitada}")

                # Repoe o estoque
                aumentar_quantidade(estoque, nome_jogo)  # Compra 10 unidades
  
                print(f"Um pedido de reposicao do estoque já foi realizado")

            else:
                diminuir_quantidade(estoque, nome_jogo, quantidade_solicitada) # Remove/Vende todas unidades solicitadas

                print(f"O jogo {nome_jogo} foi comprado com sucesso")
                print(f"Quantidade restante: {quantidade_disponivel - quantidade_solicitada}")

        else:
            print(f"O jogo {nome_jogo} não esta presente no estoque.")
            erro_cadastro+=1
        
        print('--')

    # Retorno    
    if erro_quantidade >= 1 and erro_cadastro >= 1:
        print("1 ou mais jogos sem cadastro e/ou com quantidade insuficiente")
        return -7 # 1+ jogos sem cadastro e/ou quantidade insuficiente
    
    elif erro_quantidade >= 1:
        print("1 ou mais erros de quantidade foram gerados durante a solicitacao de compra")
        return -5 # 1+ quantidade insuficiente
    
    elif erro_cadastro >= 1:
        print("1 ou mais jogos sem cadastro encontrados durante a solicitacao de compra.")
        return -6 # 1+ jogos sem cadastro
    
    else:
        print("Todas as compras foram realizadas com sucesso")
        return 1 # Sucesso

"""
Estrutura do arquivo json utilizado:
Em "estoque", "nome" : "quantidade"
Em "catalogo", "nome" : "preco"
{
    "estoque" : {
        "jogo_um" : 4,
        "jogo_dois" : 1,
        ...
    },
    "catalogo" : {
        "jogo_um" : 7.2,
        "jogo_dois" : 8.6,
        ...
    }
"""


"""
** Objetivo: Restaurar a estrutura persistida em arquivo .json referente ao estoque
** Descrição detalhada:
- Valida o tipo do primeiro parâmetro
- Valida o arquivo de nome passado por parâmetro
- Inicializa um dicionário vazio
- Abre o arquivo e carrega para uma estrutura de dicionário
- Acessa o campo de estoque
- Insere cada valor de estoque na estrutura de estoque
- Retorna a estrutura
** Acoplamento
* Parâmetro:
- arquivo_estrutura -> str: nome do arquivo que deve ser aberto
* Retornos:
- -16: arquivo_estrutura não é string
- -17: json vazio
- -18: arquivo com formato inválido
** Condições de acoplamento:
* Assertivas de entrada:
- O programa inicializou e não tem nenhuma estrutura de estoque carregada em memória
* Assertivas de saída:
- A função retorna a estrutura restaurada do arquivo para a memória principal
- A estrutura retornada é referente ao estoque
* Interface com o usuário:
- 
"""
@validaArg
def restaura_estrutura_estoque(arquivo_estrutura, estoque):
    # if not isinstance(arquivo_estrutura, str):
    #     return -16 # arquivo_estrutura não é string
    # if verificar_json(arquivo_estrutura) == 0:
    #     # print("Arquivo da estrutura está vazio")
    #     return -17
    # if verificar_json(arquivo_estrutura) == -1:
    #     # print("Arquivo da estrutura tem formato invalido")
    #     return -18

    with open(arquivo_estrutura) as f:
        json_arquivo = json.load(f)
        
        arquivo_est_estoque = json_arquivo["estoque"]
    
        for nome in arquivo_est_estoque.keys():
            inserir_jogo(estoque, nome, arquivo_est_estoque[nome])
    
    return 1

"""
** Objetivo: Restaurar a estrutura persistida em arquivo .json referente ao catalogo
** Descrição detalhada:
- Valida o tipo do primeiro parâmetro
- Valida o arquivo de nome passado por parâmetro
- Inicializa um dicionário vazio
- Abre o arquivo e carrega para uma estrutura de dicionário
- Acessa o campo de catalogo
- Insere cada valor de catalogo na estrutura de catalogo
- Retorna a estrutura
** Acoplamento
* Parâmetro:
- arquivo_estrutura -> str: nome do arquivo que deve ser aberto
* Retornos:
- -16: arquivo_estrutura não é string
- -17: json vazio
- -18: arquivo com formato inválido
** Condições de acoplamento:
* Assertivas de entrada:
- O programa inicializou e não tem nenhuma estrutura de catalogo carregada em memória
* Assertivas de saída:
- A função retorna a estrutura restaurada do arquivo para a memória principal
- A estrutura retornada é referente ao catálogo
* Interface com o usuário:
- 
"""
@validaArg
def restaura_estrutura_catalogo(arquivo_estrutura, catalogo):
    # if not isinstance(arquivo_estrutura, str):
    #     return -16 # arquivo_estrutura não é string
    # if verificar_json(arquivo_estrutura) == 0:
    #     # print("Arquivo da estrutura está vazio")
    #     return -17
    # if verificar_json(arquivo_estrutura) == -1:
    #     # print("Arquivo da estrutura tem formato invalido")
    #     return -18
    
    with open(arquivo_estrutura) as f:
        json_arquivo = json.load(f)

        arquivo_est_catalogo = json_arquivo["catalogo"]
                     
        for nome in arquivo_est_catalogo.keys():
            cadastrar(catalogo, nome, arquivo_est_catalogo[nome])
    
    return 1

# Funcao auxiliar para verificar o arquivo .json a partir do nome (xxxxx.json)
@validaArg
def verificar_json(nome_arquivo):
    # Verifica a extensao do arquivo
    if not nome_arquivo.endswith('.json'):
        return -3  # Formato de arquivo invalido

    try:
        # Abre o arquivo
        with open(nome_arquivo) as file:
            data = json.load(file)
            
            # Checa se o arquivo esta vazio
            if not data:
                return -2  # JSON vazio

            return 0  # JSON valido
    except FileNotFoundError:
        return -3  # Formato de arquivo invalido
    except json.JSONDecodeError:
        return -3  # Formato de arquivo invalido
    
  
"""
Estrutura dos dicionarios esperados:
estoque = {"nome" : "quantidade"}
catalogo = {"nome" : "preco"}

Ex. da estutura do .json que sera montado:
dados =
{
    "estoque" : {
        "jogo_um" : 4,
        "jogo_dois" : 1,
        ...
    },
    "catalogo" : {
        "jogo_um" : 7.2,
        "jogo_dois" : 8.6,
        ...
    }


** Objetivo: Persistir os dados e cria o arquivo .json
** Descrição detalhada:
- Valida o tipo e estrutura do parametro recebido (Espera dois dicionarios)
- Abre o .json para (sobre)escrever as informacoes recebidas
- Retorna o codigo de acordo com o resultado da operacao
** Acoplamento
* Parâmetro:
- estoque -> dict: Contem as informacoes dos produtos (nome e quantidade em estoque)
- catalogo -> dict: Contem as informacoes dos produtos (nome e preco)
* Retornos:
- 1 #Sucesso
- -8 # Parametro recebido nao é um dicionario
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 2 parâmetros
- Recebe um dicionario contendo, na estrutura correta, as informacoes sobre quantidade de cada produto.
- Recebe um segundo dicionario contendo preco de cada produto
* Assertivas de saída:
- Sobrescreve o .json e retorna o codigo de erro
- Nome do .json eh conhecido, logo nao deve ser retornado
"""
@validaArg
def persiste_estrutura(estoque, catalogo):
    if not isinstance(estoque, dict) or not isinstance(catalogo, dict):
        print("Parametro invalido. O parametro recebido nao e um dicionario") # Parametro recebido nao é um dicionario
        return -8

    dados = {
        "estoque": estoque,
        "catalogo": catalogo
    }
     
    with open('estrutura.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    print("Sucesso ao persistir os dados") #.json montado corretamente
    return 1

@validaArg
def gera_log(dict_log):
    if not isinstance(dict_log,dict):
        print("Parametro invalido")
        return -4
    f = open("Log.json", "w")
    dict_log_json = json.dumps(dict_log)
    f.write(dict_log_json)
    f.close()
    return 0

