perguntas = [ ['Seu animal late?', 'cachorro'] ]


while True:
    print('Pense em um animal e eu tentarei adivinhar qual é!...')
    print()

    acertou = False # variável para controlar se o programa acertou o animal
    for pergunta in perguntas:
        resposta = input(f'{pergunta[0]} (s/n):  ')
        if resposta.lower() == 's': # o .lower() transforma a resposta em minúscula
            print(f'Você pensou em {pergunta[1]}!')
            acertou = True
            break

    if not acertou: # se o programa não acertou o animal vai executar esse bloco abaixo:
        animal = input('Hoje não estou com sorte! Em qual animal você pensou?: ')
        novapergunta = input('Qual pergunta eu poderia ter feito para descobrir em qual animal você pensou?: ')

        perguntas.append([novapergunta, animal])

    resposta = input('Quer jogar novamente? (s/n): ')
    if resposta.lower() != 's':
        print('Obrigado por jogar! Até a próxima!')
        break
