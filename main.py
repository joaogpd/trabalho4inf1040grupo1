import modules.catalogo.catalogo as catalogo
import modules.estoque.estoque as estoque
import modules.tratamentojson.tratamentojson as tjson

def main():
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
	tjson.persiste_estruturas(est_estoque, est_catalogo); 
        print("Escolha uma opção: ")
        # inserir_catalogo inserir_estoque remover_estoque exibir_estoque exibir_catalogo 
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
			func(nome, est_estoque)
		    else:
                        print("Estoque: ")
                        func(est_estoque)
                elif "inserir" in escolha:
                    nome = input("Nome: ")
                    # quantidade = input("Quantidade: ")
                    func(est_estoque, nome)
	        elif "remover" in escolha:
		    nome = input("Nome: ")
		    func(est_estoque, nome)
		elif "quantidade" in escolha:
		    quantidade = input("Quantidade: ")
		    nome = input("Nome: ")
		    func(est_estoque, nome, quantidade)
            elif "catalogo" in escolha:
		if "alterar" in escolha:
		    nome = input("Nome: ")
		    if "nome" in escolha:
			nome_novo = input("Nome novo: ")
			func(est_estoque, nome, nome_novo)
             	    elif "preco" in escolha:
			preco_novo = input("Preco novo: ")
			func(est_estoque, nome, preco_novo)
		elif "exibir" in escolha:
		        func(est_catalogo)
		elif "cadastrar" in escolha:
			nome = input("Nome: ")
			preco = input("Preco: ")
  			func(est_catalogo, nome, preco)
	    elif "pedidos" in escolha:
		if "jogos_novos" in "escolha":
			# func()
		elif "compras" in "escolha":
			# func()
		

 

if __name__ == '__main__':
    main()
