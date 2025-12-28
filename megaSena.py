#Cálculo da probabilidade de ganhar na Mega-Sena com um número específico de jogos simples.

import math

def combinacoes(n, k):
    return math.comb(n, k)

numeros_totais = 60
numeros_escolhidos = 6
quantidade_jogos = 192  # número de jogos simples

total_combinacoes = combinacoes(numeros_totais, numeros_escolhidos)

# chance considerando vários jogos
chance = quantidade_jogos / total_combinacoes

print(f'Total de combinações possíveis: {total_combinacoes:,}'.replace(',', '.'))
print(f'Chance de ganhar com {quantidade_jogos} jogos: 1 em {(total_combinacoes / quantidade_jogos):,.0f}'.replace(',', '.'))
print(f'Probabilidade percentual: {chance * 100:.8f}%')
