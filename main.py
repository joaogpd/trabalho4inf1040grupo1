import modules.catalogo.catalogo as catalogo
import modules.estoque.estoque as estoque
import modules.tratamentojson.tratamentojson as tjson

def main():
    dict_erros = {
	    1: "Sucesso",
	    0: "Jogo nao encontrado",
	    -1: "Nome invalido",
	    -2: "arquivo vazio",
	    -3: "arquivo invalido",
	    -4: "estrutura invalida",
	    -5: "1+ quantidade insuficiente",
	    -6: "1+ jogos sem cadastro",
	    -7: "1+ jogos sem cadastro e/ou quantidade insuficiente",
	    -8: "valor passado não é dict",
	    -9: "dicionário vazio",
	    -10: "valor de estrutura não é dict",
	    -11: "valor de nome não é str",
	    -12: "nome não presente na estrutura",
	    -13: "valor de estrutura passada não é dict",
	    -14: "valor de nome passado não é str",
	    -15: "valor de preco_novo passado não é numeric",
	    -16: "arquivo_estrutura não é string",
	    -17: "json vazio",
	    -18: "arquivo com formato inválido"
    }

    dict_log = dict()
	
    # est_estoque = tjson.restaura_estrutura_estoque()
    # est_catalogo = tjson.restaura_estrutura_catalogo()
    est_estoque = dict()
    est_catalogo = dict()
    opcoes = {"exibir_estoque" : estoque.exibe_todos_estoque, "inserir_estoque" : estoque.inserir_jogo, \
	      "remover_estoque" : estoque.remover_jogo, "exibir_jogo_estoque" : estoque.exibe_jogo, "diminuir_quantidade" : estoque.diminuir_quantidade, \
	      "aumentar_quantidade" : estoque.aumentar_quantidade, "alterar_nome_catalogo" : catalogo.alterar_nome, "alterar_preco_catalogo" : catalogo.alterar_preco, \
	      "exibir_catalogo" : catalogo.exibe_todos_catalogo, "cadastrar_catalogo" : catalogo.cadastrar, "ler_pedidos_jogos_novos" : tjson.tratar_pedidos_novojogo, \
	      "ler_pedidos_compras" : tjson.tratar_solicitacao_compra}
    while True:
		tjson.persiste_estrutura(est_estoque, est_catalogo)
        print("Escolha uma opção: ")
        for i in opcoes.keys():
            print(i, end=" ")
        print("")
        escolha = input()
        if escolha not in opcoes.keys():
            if escolha == "quit":
                break
            print("Opção desconhecida")
            continue
        else:
            func = opcoes[escolha]
            if "estoque" in escolha:
                if "exibir" in escolha:
		    		if "jogo" in escolha:
						nome = input("Nome: ")
						ret = func(nome, est_estoque)
						dict_log[escolha] = dict_erros[ret]
		    		else:
                        print("Estoque: ")
                        ret = func(est_estoque)
						dict_log[escolha] = dict_erros[ret]
                elif "inserir" in escolha:
                    nome = input("Nome: ")
                    # quantidade = input("Quantidade: ")
                    ret = func(est_estoque, nome)
		    		dict_log[escolha] = dict_erros[ret]
	        	elif "remover" in escolha:
		    		nome = input("Nome: ")
		    		ret = func(est_estoque, nome)
		    		dict_log[escolha] = dict_erros[ret]
				elif "quantidade" in escolha:
		    		quantidade = input("Quantidade: ")
		    		nome = input("Nome: ")
		    		ret = func(est_estoque, nome, quantidade)
		    		dict_log[escolha] = dict_erros[ret]
            elif "catalogo" in escolha:
				if "alterar" in escolha:
		    		nome = input("Nome: ")
		    		if "nome" in escolha:
						nome_novo = input("Nome novo: ")
						ret = func(est_estoque, nome, nome_novo)
						dict_log[escolha] = dict_erros[ret]
             	    elif "preco" in escolha:
						preco_novo = input("Preco novo: ")
						ret = func(est_estoque, nome, preco_novo)
						dict_log[escolha] = dict_erros[ret]
				elif "exibir" in escolha:
		        	ret = func(est_catalogo)
					dict_log[escolha] = dict_erros[ret]
				elif "cadastrar" in escolha:
					nome = input("Nome: ")
					preco = input("Preco: ")
  					ret = func(est_catalogo, nome, preco)
					dict_log[escolha] = dict_erros[ret]
	    	elif "pedidos" in escolha:
				if "jogos_novos" in "escolha":
					# func()
				elif "compras" in "escolha":
					# func()
    gera_log(dict_log)

 

if __name__ == '__main__':
    main()
