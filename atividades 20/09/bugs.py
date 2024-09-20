bugs_reportados = [
    {"bug_id": " 01", "gravidade": "Alta", "contagem": 9},
    {"bug_id": "Bug 02", "gravidade": "Média", "contagem": 8},
    {"bug_id": "Bug 03", "gravidade": "Baixa", "contagem": 3},
    {"bug_id": "Bug 04", "gravidade": "Alta", "contagem": 6},
    {"bug_id": "Bug 05", "gravidade": "Crítica", "contagem": 20},
    {"bug_id": "Bug 06", "gravidade": "Baixa", "contagem": 7},
    {"bug_id": "Bug o7", "gravidade": "Crítica", "contagem": 19}
]

bugs_por_gravidade = {}
for bug in bugs_reportados:
    gravidade = bug["gravidade"]
    if gravidade not in bugs_por_gravidade:
        bugs_por_gravidade[gravidade] = []
    bugs_por_gravidade[gravidade].append(bug)

bugs_prioritarios = [bug for bug in bugs_reportados if bug["contagem"] > 5]

def gerar_relatorio():
    print(" Relatório Semanal de Bugs ")
    
    for gravidade, bugs in bugs_por_gravidade.items():
        print(f"\nBugs com gravidade {gravidade}:")
        for b in bugs:
            print(f"  {b['bug_id']} - Reportado {b['contagem']} vezes")

    print("\nBugs Prioritários (reportados mais de 6 vezes):")
    for bug in bugs_prioritarios:
        print(f"{bug['bug_id']} - gravidade: {bug['gravidade']} - Reportado {bug['contagem']} vezes")

gerar_relatorio()