import modules.catalogo.catalogo as catalogo
import modules.estoque.estoque as estoque
import modules.tratamentojson.tratamentojson as tratamentojson

def main():
    # est_estoque = estoque.restaura_estrutura_estoque()
    # est_catalogo = catalogo.restaura_estrutura_catalogo()
    est_estoque = dict()
    est_catalogo = dict()
    opcoes = {"exibir_estoque" : estoque.exibe_todos_estoque, "exibir_catalogo" : catalogo.exibe_todos_catalogo, "inserir_estoque" : estoque.inserir_jogo }
    while True:
        print("Escolha uma opção: ")
        # inserir_catalogo inserir_estoque remover_estoque exibir_estoque exibir_catalogo"
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
                    print("estoque: ")
                    func(est_estoque)
                else:
                    nome = input("Nome: ")
                    # quantidade = input("Quantidade: ")
                    func(est_estoque, nome)
            elif "catalogo" in escolha:
                func(est_catalogo)

if __name__ == '__main__':
    main()
