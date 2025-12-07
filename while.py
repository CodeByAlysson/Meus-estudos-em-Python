# Vamos aprender a usar o loop while em Python!
# O while permite executar um bloco de código repetidamente
# enquanto uma condição for verdadeira.

print("Olá! Vamos explorar o uso do loop while em Python.")

soma = 0
n = 1

while n <= 10: # enquanto n for menor ou igual a 10
    soma += n  # soma recebe soma mais n
    n += 1     # n recebe n mais 1

print(soma) # imprime o valor da soma

# Agora, vamos ver um exemplo de loop while que depende da entrada do usuário.

resposta = "" # inicializa a variável resposta como uma string vazia
while resposta.lower() != "sair": # enquanto resposta for diferente de "sair"
    resposta = input("Digite 'sair' para encerrar o loop: ") # pede ao usuário para digitar "sair"
    print(f"Você digitou: {resposta}") # imprime o que o usuário digitou

print("Loop encerrado.")