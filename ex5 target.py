firstString = input("Digite uma palavra: ") # Solicita ao usuário uma string

invertString = "" # Armazena a string invertida

for char in firstString[::-1]: # Inverte a string
    invertString += char # Adiciona o caractere na string invertida

print("Palavra invertida:", invertString) # Exibe a string invertida