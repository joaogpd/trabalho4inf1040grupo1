"""
** Objetivo: Tratar a solicitacao (arquivo json) de compra de jogos
** Descrição detalhada:
- Valida o arquivo recebido
- Faz a movimentacao de compra e venda necessaria
- Retorna o codigo equivalente ao resultado das movimentacoes
** Acoplamento
* Parâmetro:
- solicitacao -> json: 
- estoque -> dict: estrutura que deve ter nome e quantidade de cada jogo
- preco -> dict: estrutura que deve ter nome e preco de cada jogo
* Retornos:
-  1 # Sucesso
- -2 # Arquivo vazio
- -3 # Arquivo invalido
- -5 # 1+ quantidade insuficiente
- -6 # 1+ jogos sem cadastro
- -7 # 1+ jogos sem cadastro e/ou quantidade insuficiente
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe 3 parâmetros
- Precisa das funcoe auxiliares, verificar_json, aumentar_quantidade e diminuir_quantidade
* Assertivas de saída:
- Realiza as operacoes (compra/venda) necessaria e retorna o codigo correspondente
- Arquivo de solicitacao JSON será descartado, entao nao é preciso fazer nada com ele
"""

# Solicitacao considerada:
# solicitacao.json =
# '''
# {
#   "jogos": [
#         {"nome": "Jogo1", "quantidade": 2},
#         {"nome": "Jogo2", "quantidade": 1},
#         {"nome": "Jogo3", "quantidade": 4}
#     ]
# }
# '''
# Estruturas consideradas:
# estoque = {
#     "Jogo1": 3,
#     "Jogo2": 0,
#     "Jogo3": 2
# }
#
# preco = {
#     "Jogo1": 20.65,
#     "Jogo2": 10.99,
#     "Jogo3": 12.25
# }



def tratar_solicitacao_compra(solicitacao, estoque, preco):

    erro_quantidade = 0
    erro_cadastro = 0

    #Verifica o arquivo de solicitacao
    if verificar_json(solicitacao) == 0:
        print("Arquivo de solicitacao .json está vazio")
        return -2 #Arquivo vazio
    
    elif verificar_json(solicitacao) == -1:
        print("Arquivo de solicitacao nao é um .json")
        return -3 #Arquivo invalido
    

    for jogo in solicitacao['jogos']:
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


'''
** Objetivo: Verificar o arquivo json recebido
** Descrição detalhada:
- Valida o arquivo recebido
- Retorna o codigo equivalente ao resultado encontrado
** Acoplamento
* Parâmetro:
- nome_arquivo -> json: 
* Retornos:
- 1  # É um .JSON não vazio
- 0  # JSON vazio
- -1 # Não é um .JSON
** Condições de acoplamento:
* Assertivas de entrada:
- A função recebe um arquivo
* Assertivas de saída:
- Verifica o formato e a integridade do arquivo recebido e retorna o codigo equivalente
'''

import json
def verificar_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        try:
            conteudo = arquivo.read()
            if not conteudo:
                return 0  # JSON vazio

            json.loads(conteudo)
            return 1  # É um .JSON não vazio
        
        except (json.JSONDecodeError, UnicodeDecodeError):
            return -1  # Não é um .JSON
