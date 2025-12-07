# Arrays em Python são estruturas que guardam vários valores em uma única variável, 
# organizados em sequência.
# Você acessa cada valor pelo índice (posição), começando do 0.

numeros = [3, 6, 9]  # Cria um array (lista) com três números
numeros[0]  # Acessa o primeiro número (3)
print(f"O primeiro número é {numeros[0]}")


numeros[0] = 7  # Modifica o primeiro número para 7 usando [] e indicando a posição
print(numeros)  # Imprime o array modificado: [7, 6, 9]

# Você pode adicionar novos valores ao array usando o método append()
numeros.append(12)  # Adiciona o número 12 ao final do array
print(numeros)  # Imprime o array modificado: [7, 6, 9, 12]

# Exemplos adicionais do método append()

# Exemplo 1: Adicionando diferentes tipos de dados
frutas = ["maçã", "banana"]
print(f"Lista inicial de frutas: {frutas}")

frutas.append("laranja")  # Adiciona uma string ao final
print(f"Após adicionar laranja: {frutas}")

frutas.append("uva")  # Adiciona outra fruta
print(f"Após adicionar uva: {frutas}")

# Exemplo 2: Construindo um array vazio com append()
notas = []  # Cria um array vazio
print(f"Array vazio de notas: {notas}")

notas.append(8.5)  # Adiciona primeira nota
notas.append(9.0)  # Adiciona segunda nota
notas.append(7.5)  # Adiciona terceira nota
print(f"Notas adicionadas: {notas}")

# Exemplo 3: Usando append() dentro de um loop
pares = []  # Array para armazenar números pares
print("Adicionando números pares de 0 a 10:")

for numero in range(0, 11):
    if numero % 2 == 0:  # Verifica se o número é par
        pares.append(numero)  # Adiciona o número par ao array
        print(f"Número {numero} adicionado")

print(f"Array final de números pares: {pares}")

# Exemplo 4: Append com entrada do usuário (comentado para não precisar de interação)
# nomes = []
# for i in range(3):
#     nome = input(f"Digite o nome {i+1}: ")
#     nomes.append(nome)
# print(f"Nomes inseridos: {nomes}")

# Observação importante: append() sempre adiciona elementos ao FINAL do array
# Para adicionar em outras posições, use insert()

# fim do arquivo arrays.py 