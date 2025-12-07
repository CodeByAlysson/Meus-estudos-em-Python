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

# fim do arquivo arrays.py 