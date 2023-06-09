import json

__all__ = ["tratar_solicitacao_compra", "restaura_estrutura", "persiste_estrutura_estoque"]

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
- -1: arquivo_estrutura não é string
- -2: json vazio
- -3: arquivo com formato inválido
** Condições de acoplamento:
* Assertivas de entrada:
- O programa inicializou e não tem nenhuma estrutura de estoque carregada em memória
* Assertivas de saída:
- A função retorna a estrutura restaurada do arquivo para a memória principal
- A estrutura retornada é referente ao estoque
* Interface com o usuário:
- 
"""
def restaura_estrutura_estoque(arquivo_estrutura):
    if not isistance(arquivo_estrutura, str):
        return -1 # arquivo_estrutura não é string
    if verificar_json(arquivo_estrutura) == 0:
        # print("Arquivo da estrutura está vazio")
        return -2
    if verificar_json(arquivo_estrutura) == -1:
        # print("Arquivo da estrutura tem formato invalido")
        return -3 
 
    estrutura_estoque = dict()
    with open(arquivo_estrutura) as f:
        json_arquivo = json.load(f)
        
        arquivo_est_estoque = json_arquivo["estoque"]
    
        for nome in arquivo_est_estoque.keys():
            inserir_jogo(estrutura_estoque, nome, arquivo_est_estoque[nome])
    
    return estrutura_estoque

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
- -1: arquivo_estrutura não é string
- -2: json vazio
- -3: arquivo com formato inválido
** Condições de acoplamento:
* Assertivas de entrada:
- O programa inicializou e não tem nenhuma estrutura de catalogo carregada em memória
* Assertivas de saída:
- A função retorna a estrutura restaurada do arquivo para a memória principal
- A estrutura retornada é referente ao catálogo
* Interface com o usuário:
- 
"""
def restaura_estrutura_catalogo(arquivo_estrutura):
    if not isistance(arquivo_estrutura, str):
        return -1 # arquivo_estrutura não é string
    if verificar_json(arquivo_estrutura) == 0:
        # print("Arquivo da estrutura está vazio")
        return -2
    if verificar_json(arquivo_estrutura) == -1:
        # print("Arquivo da estrutura tem formato invalido")
        return -3 
    
    with open(arquivo_estrutura) as f:
        json_arquivo = json.load(f)

        estrutura_catalogo = dict()
        arquivo_est_catalogo = json_arquivo["catalogo"]
                     
        for nome in arquivo_est_catalogo.keys():
            cadastrar(estrutura_catalogo, nome, arquivo_est_catalogo[nome])
    
    return estrutura_catalogo                 


# Funcao auxiliar para verificar o arquivo .json a partir do nome (xxxxx.json)
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
Estrutura do dicionario esperado:
"estoque" {"nome" : "quantidade"}
"catalogo" {"nome" : "preco"}

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


** Objetivo: Persistir os dados e criar o arquivo .json
** Descrição detalhada:
- Valida o tipo e estrutura do parametro recebido (Espera um dicionario)
- Abre o .json para (sobre)escrever as informacoes recebidas
- Retorna o codigo de acordo com o resultado da operacao
** Acoplamento
* Parâmetro:
- dados -> dict: Contem as informacoes dos produtos (quantidade em estoque e preco)
* Retornos:
- 1 #Sucesso
- -3 #Parametro invalido
- -4 #Estrutura do dict invalida
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 1 parâmetro
- Recebe um dicionario contendo, na estrutura correta, as informacoes sobre preco e quantidade de cada produto
* Assertivas de saída:
- Sobrescreve o .json e retorna o codigo de erro
- Nome do .json eh conhecido, logo nao deve ser retornado
- 
"""
def persiste_estrutura_estoque(dados):
    if not isinstance(dados, dict):
        print("Arquivo invalido. O parametro recebido nao e um dict") #Arquivo recebido nao e um dict
        return -3
    
    elif "estoque" not in dados or "catalogo" not in dados:
        print("Estrutura invalida. O dicionario nao esta de acordo com o padrao") #Dicionario recebido nao possui a estrutura correta
        return -4
    
    with open('estrutura.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    print("Sucesso ao persistir os dados") #.json montado corretamente
    return 1

