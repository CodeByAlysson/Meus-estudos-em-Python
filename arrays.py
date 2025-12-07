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

# Vamos explorar mais sobre o método append()
print("\n--- Explorando o método append() ---")

# Criando uma lista vazia e adicionando elementos
frutas = []
print(f"Lista inicial (vazia): {frutas}")

frutas.append("maçã")
print(f"Depois de adicionar 'maçã': {frutas}")

frutas.append("banana")
print(f"Depois de adicionar 'banana': {frutas}")

frutas.append("laranja")
print(f"Depois de adicionar 'laranja': {frutas}")

# Você pode usar append() em um loop para adicionar vários elementos
print("\n--- Usando append() em um loop ---")
pares = []
for i in range(2, 11, 2):  # Números pares de 2 a 10
    pares.append(i)
    print(f"Adicionando {i}, lista atual: {pares}")

print(f"\nLista final de números pares: {pares}")

# Exemplo prático: construindo uma lista de tarefas
print("\n--- Exemplo prático: Lista de tarefas ---")
tarefas = []
tarefas.append("Estudar Python")
tarefas.append("Fazer exercícios")
tarefas.append("Revisar código")

print("Minhas tarefas:")
for i, tarefa in enumerate(tarefas, 1):
    print(f"{i}. {tarefa}")
