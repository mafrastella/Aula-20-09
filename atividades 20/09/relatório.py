
vendas_diarias = [
    ("Produto A", 10),
    ("Produto B", 20),
    ("Produto A", 15),
    ("Produto C", 5),
    ("Produto B", 25),
    ("Produto A", 30),
    ("Produto C", 10),
    ("Produto B", 15),
]

totais_vendas = {}
dias_vendas = {}

for produto, vendas in vendas_diarias:
    
    if produto not in totais_vendas:
        totais_vendas[produto] = 0
        dias_vendas[produto] = 0  
    totais_vendas[produto] += vendas
    dias_vendas[produto] += 1

print("Relatório de Vendas")
for produto in totais_vendas:
    total = totais_vendas[produto]
    dias = dias_vendas[produto]
    media = total / dias  

    print(f"{produto}: Total de Vendas = {total}, Média de Vendas Diárias = {media:.2f}")
