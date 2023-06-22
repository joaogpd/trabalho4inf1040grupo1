import modules.catalogo.catalogo as catalogo
import modules.estoque.estoque as estoque
import modules.tratamentojson.tratamentojson as tjson

def main():
    dict_erros = {
        1: "Sucesso",
        0: "Jogo não encontrado",
        -1: "Nome inválido",
        -2: "Arquivo vazio",
        -3: "Arquivo inválido",
        -4: "Estrutura inválida",
        -5: "Quantidade insuficiente",
        -6: "Jogos sem cadastro",
        -7: "Jogos sem cadastro e/ou quantidade insuficiente",
        -8: "Valor passado não é dict",
        -9: "Dicionário vazio",
        -10: "Valor de estrutura não é dict",
        -11: "Valor de nome não é str",
        -12: "Nome não presente na estrutura",
        -13: "Valor de estrutura passado não é dict",
        -14: "Valor de nome passado não é str",
        -15: "Valor de preco_novo passado não é numeric",
        -16: "arquivo_estrutura não é string",
        -17: "JSON vazio",
        -18: "Arquivo com formato inválido"
    }

    dict_log = dict()

    est_estoque = dict()
    est_catalogo = dict()
    tjson.restaura_estrutura_estoque("estrutura.json", est_estoque)
    tjson.restaura_estrutura_catalogo("estrutura.json", est_catalogo)
    opcoes = {"exibir_estoque" : estoque.exibe_todos_estoque, "inserir_estoque" : estoque.inserir_jogo, 
	          "remover_estoque" : estoque.remove_jogo, "exibir_jogo_estoque" : estoque.exibe_jogo, "diminuir_quantidade_estoque" : estoque.diminuir_quantidade, 
	          "aumentar_quantidade_estoque" : estoque.aumentar_quantidade, "alterar_nome_catalogo" : catalogo.alterar_nome, "alterar_preco_catalogo" : catalogo.alterar_preco, 
	          "exibir_catalogo" : catalogo.exibe_todos_catalogo, "cadastrar_catalogo" : catalogo.cadastrar, "ler_pedidos_jogos_novos" : tjson.tratar_pedidos_novojogo, 
	          "ler_pedidos_compras" : tjson.tratar_solicitacao_compra}
    
    while True:
        tjson.persiste_estrutura(est_estoque, est_catalogo)
        print("\nEscolha uma opção: ")
        for i in opcoes.keys():
            print(i, end="  ")
        print("")
        print("\nDigite quit para sair")
        escolha = input()
        if escolha not in opcoes.keys():
            if escolha == "quit":
                break
            print(f"Opção desconhecida '{escolha}'")
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
                    ret = func(est_estoque, nome)
                    dict_log[escolha] = dict_erros[ret]
                elif "quantidade" in escolha:
                    nome = input("Nome: ")
                    if "diminuir" in escolha:
                        quantidade = int(input("Quantidade: "))
                        ret = func(est_estoque, nome, quantidade)
                    elif "aumentar" in escolha:
                        ret = func(est_estoque, nome)
                    dict_log[escolha] = dict_erros[ret]
            elif "catalogo" in escolha:
                if "alterar" in escolha:
                    nome = input("Nome: ")
                    if "nome" in escolha:
                        nome_novo = input("Nome novo: ")
                        ret = func(est_estoque, nome, nome_novo)
                        dict_log[escolha] = dict_erros[ret]
                    if "preco" in escolha:
                        preco_novo = float(input("Preco novo: "))
                        ret = func(est_estoque, nome, preco_novo)
                elif "exibir" in escolha:
                    print("Catalogo: ")
                    ret = func(est_catalogo)
                    dict_log[escolha] = dict_erros[ret]
                elif "cadastrar" in escolha:
                    nome = input("Nome: ")
                    preco = float(input("Preco: "))
                    ret = func(est_catalogo, nome, preco)
                    dict_log[escolha] = dict_erros[ret]
            elif "pedidos" in escolha:
                if "jogos_novos" in escolha:
                    nome_arquivo = input("Insira o nome do arquivo: ")
                    func(nome_arquivo, est_estoque, est_catalogo)
                elif "compras" in escolha:
                    nome_arquivo = input("Insira o nome do arquivo: ")
                    func(nome_arquivo, est_estoque)
            
    tjson.gera_log(dict_log)
                
        
if __name__ == '__main__':
    main()
