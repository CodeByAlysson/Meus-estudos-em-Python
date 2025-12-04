# Hoje vamos aprender a usar match e case em Python!
# O match serve para comparar um valor com diferentes padrões,
# e o case define o que fazer para cada padrão correspondente.

print("Olá! Vamos explorar o uso de match e case em Python.")
print()

comando = input("Digite o comando desejado: play, pause ou continuar: ")

match comando:
    case "play":
        print("▶️  Tocando...")
    case "pause":
        print("⏸  Pausado...")
    case "continuar":
        print("▶️  Continuando...")
    case "parar":
        print("⏹  Parado.")
    case _:
        print("❓ Comando não reconhecido!")
