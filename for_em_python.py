# Vamos aprender a usar o loop for em Python!
# Este código calcula a soma dos primeiros 10 números inteiros usando um loop for.

print("Olá! Vamos explorar o uso do for em Python.")

soma = 0
n = 1

for i in range(1, 11):  # range(1, 11) gera números de 1 a 10
    soma += i  # Adiciona o valor de i à soma
    print(f"Adicionando {i}, soma atual é {soma}")  # Imprime o valor de i e a soma atual