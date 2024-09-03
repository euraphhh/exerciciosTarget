faturamento = { # Cria um dicionário com o faturamento mensal de cada estado
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento.values()) # Calcula o faturamento total mensal

for estado, valor in faturamento.items(): # Itera sobre o dicionário
    print(f"{estado}: {valor / total_mensal * 100:.2f}%") # Imprime o percentual de faturamento de cada estado