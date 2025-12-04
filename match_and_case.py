# Hoje vamos aprender a usar match e case em Python!
# O match serve para comparar um valor com diferentes padrões,
# e o case define o que fazer para cada padrão correspondente.

print("Olá! Vamos explorar o uso de match e case em Python.")
print()

comando = input("Digite o comando desejado: Iniciar, Parar ou Continuar: ")

match comando: 
    case "Iniciar":
        print("O sistema está iniciando...")
    case "Parar":
        print("O sistema está parando...")
    case "Continuar":
        print("O sistema está continuando...")
    case _:
        print("Comando inválido!")