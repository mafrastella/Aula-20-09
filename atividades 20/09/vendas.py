# Simulando dados de vendas mensais dos produtos
vendas_mensais = {
    "Produto A": [100, 150, 200, 250, 300, 350],
    "Produto B": [200, 180, 160, 140, 120, 100],
    "Produto C": [300, 300, 320, 330, 350, 360],
    "Produto D": [400, 390, 380, 370, 360, 350],
}

tendencias_aumento = []
tendencias_diminuição = []

for produto, vendas in vendas_mensais.items():
    aumento_continuo = True
    diminuicao_continua = True

    for i in range(1, len(vendas)):
        if vendas[i] <= vendas[i - 1]:  
            aumento_continuo = False
        if vendas[i] >= vendas[i - 1]:  
            diminuicao_continua = False

    if aumento_continuo:
        tendencias_aumento.append(produto)
    elif diminuicao_continua:
        tendencias_diminuição.append(produto)

print("Produtos com aumento contínuo nas vendas:", tendencias_aumento)
print("Produtos com diminuição contínua nas vendas:", tendencias_diminuição)