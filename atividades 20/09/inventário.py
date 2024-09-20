def gerenciar_inventario():
    quantidade_itens = int(input("Quantos itens deseja adicionar ao inventário? "))
    
    inventario = []
    
    for i in range(quantidade_itens):
        print(f"\nInserindo dados para o item {i + 1}:")
        nome = input("Nome do equipamento: ")
        categoria = input("Categoria do equipamento: ")
        quantidade = int(input("Quantidade: "))
        
        item = {
            "nome": nome,
            "categoria": categoria,
            "quantidade": quantidade
        }
        inventario.append(item)

    print("\n Inventário Completo")
    for item in inventario:
        print(f"Nome: {item['nome']}, Categoria: {item['categoria']}, Quantidade: {item['quantidade']}")

gerenciar_inventario()
