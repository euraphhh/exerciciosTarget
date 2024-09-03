n = int(input("Digite um número: ")) # Recebe a variável n do usuário

if n < 0: # Se n for menor que 0
    print(f"O número {n} não pertence à sequência de Fibonacci.") # Exibe que o número não pertence à sequência de Fibonacci
else: # Senão
    a, b = 0, 1 # Atribui 0 a A e 1 a B
    while b < n: # Enquanto B for menor que n
        a, b = b, a + b # Atribui B a A e a soma de A e B a B
    
    if b == n or n == 0: # Se B for igual a n ou n for igual a 0
        print(f"O número {n} pertence à sequência de Fibonacci.") # Exibe que o número pertence à sequência de Fibonacci
    else: # Senão
        print(f"O número {n} não pertence à sequência de Fibonacci.") # Exibe que o número não pertence à sequência de Fibonacci