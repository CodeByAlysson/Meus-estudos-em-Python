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

numeros.sort()  # Ordena o array em ordem crescente
print(numeros)  # Imprime o array ordenado: [6, 7, 9, 12]

numeros.reverse()  # Inverte a ordem dos elementos no array
print(numeros)  # Imprime o array invertido: [12, 9, 7, 6]

numeros.pop()  # Remove o último elemento do array
print(numeros)  # Imprime o array após a remoção: [12, 9, 7]    

numeros.insert(1, 15)  # Insere o número 15 na posição 1
print(numeros)  # Imprime o array após a inserção: [12, 15, 9, 7]

numeros[2] = "CodeByAlysson"  # Modifica o terceiro elemento para uma string
print(numeros)  # Imprime o array após a modificação: [12, 15, "CodeByAlysson", 7]

# Podemos ainda criar uma lista dentro de outra lista (array multidimensional)

numeros.insert(2, [1, 2, 3])  # Insere uma lista na posição 2
print(numeros)  # Imprime o array após a inserção: [12, 15, [1, 2, 3], "CodeByAlysson", 7]


# fim do arquivo arrays.py 