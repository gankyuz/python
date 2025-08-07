"""Inventário de itens
Simule um estoque: cada item tem nome, quantidade e preço. Permita:

Adicionar item

Remover item

Atualizar quantidade

Ver valor total em estoque"""
dados_estoque = {}
while(True):

    menu = int(input("----MENU----\n"
                     "1.Adicionar Item\n"
                     "2.Remover Item\n"
                     "3.Atualizar quantidade\n"
                     "4.Exibir valor total em estoque\n"
                     "5.Exibir estoque\n"
                     "6.Sair\n\n"
                     "Qual deseja acessar? "))

    match menu:
# Cadastro de itens
        case 1:
            nome_item = input("Digite o nome do item: ").lower()
            quantidade_item = int(input("Digite a quantidade do item: "))
            valor_item = float(input("Digite o valor do item: "))
            dados_estoque[nome_item] = {
                "Quantidade": quantidade_item,
                "Valor": valor_item
            }
# Remoção de item
        case 2:
            item_remocao = input("Digite o nome do item que deseja remover do estoque: ").lower()
            dados_estoque.pop(item_remocao)
            for chave,valor in dados_estoque.items():
                print("Item removido, veja o estoque atualizado.\n")
                print(f"Nome: {chave}")
                print(f"Quantidade: {valor['Quantidade']}")
                print(f"Valor: R$ {valor['Valor']}\n")
# Atualizar quantidade
        case 3:
            atualizar_item = input("Digite o nome do item que deseja atualizar estoque: ").lower()
            quant_item = int(input("Digite a quantidade de itens que deseja adicionar: "))
            if atualizar_item in dados_estoque:
                dados_estoque[atualizar_item]['Quantidade'] = quant_item
            else:
                    print("Item não encontrado")
# Exibir valor total do estoque
        case 4:
            valor_total = 0
            for chave,valor in dados_estoque.items():
                valor_total += valor['Quantidade'] * valor['Valor']
            print(f"O valor total do estoque: R${valor_total:.2f}")
# Exibir estoque:
        case 5:
            for chave,valor in dados_estoque.items():
                print("ESTOQUE:\n")
                print(f"Nome: {chave}")
                print(f"Quantidade: {valor['Quantidade']}")
                print(f"Valor: R$ {valor['Valor']}\n")
        case 6:
            break
