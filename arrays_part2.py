# Podemos ainda fazer operações matemáticas com arrays.

notas = [8.0, 7.5, 9.0, 6.5, 10.0]

media = 0 # variável para armazenar a média

for nota in notas: # para cada nota na lista de notas
    media += nota # somando as notas na variável média

media /=5 # dividindo a soma das notas pela quantidade de notas

print(f"A média das notas é: {media}")