import json # Importa o módulo json para o código

with open('faturamento.json', 'r') as file: # Abre o arquivo faturamento.json em modo de leitura
    data = json.load(file) # Define uma variável que recebe o conteúdo do arquivo faturamento.json

faturamento = [dia['valor'] for dia in data if dia['valor'] > 0] # Cria uma lista com os valores de faturamento dos dias em que o valor é maior que 0
menorFaturamento, maiorFaturamento = min(faturamento), max(faturamento) # Define as variáveis menor_faturamento e maior_faturamento com os valores mínimo e máximo da lista faturamento
media = sum(faturamento) / len(faturamento) # Define a variável media_mensal com a média dos valores da lista faturamento

acimaMedia = sum(1 for valor in faturamento if valor > media) # Define a variável acima_media com a quantidade de valores da lista faturamento que são maiores que a média

print(f"Menor valor de faturamento: {menorFaturamento}") # Imprime o menor valor de faturamento
print(f"Maior valor de faturamento: {maiorFaturamento}") # Imprime o maior valor de faturamento
print(f"Dias com faturamento acima da média: {acimaMedia}") # Imprime a quantidade de dias com faturamento acima da média