# Vamos aprender a ler os ERROS em Python e como depurá-los.

def soma (a, b): # Função para somar dois números
    return a + b # Retorna a soma de a e b
print(soma(2, 3))  # Deve imprimir 5


# Vamos simular erros

def soma (a, b):
    return a + b
print(soma(2))
# """ Erro: falta um argumento. Ao executar, 
# Python mostrará um TypeError indicando que
# está faltando um argumento posicional."""

def soma (a, ): # Falta o segundo parâmetro
    return a + b
print(soma(2, 3)) 

def soma (a, b) # Erro de sintaxe: falta os dois pontos no final da definição da função.:
    return a + b
print(soma(2, 3))

def soma (a, b):
    return a + b
print(soma(2, 3)  # Erro de sintaxe: falta o parêntese de fechamento na chamada da função.