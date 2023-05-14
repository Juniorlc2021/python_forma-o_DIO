from os import system, name
import random

opcao = 's'
contadorJogadas = 0
contadorJogador = 0
contadorComputador = 0

while opcao.upper() == 'S':
    system('cls') if name == 'nt' else system('clear')

    computador = random.randint(0, 2)
    jogador = int(input('''Escolha a opção para jogar:
        [0] Pedra
        [1] Papel
        [2] Tesoura
        Digite sua escolha: '''))
    contadorJogadas+=1
    pecas = ("Pedra", "Papel", "Tesoura")
# lista multi-dimensional
# nesta lista quando o resultado for -1 o computador ganha, 1 0 jogador ganha e 0 deu empate
    
    if jogador > 2:
        resultado = 'Você escolheu uma opção inválida!'
    else:
        print('Você escolheu {}'.format(pecas[jogador]))
        print('O computador escolheu: {}'.format(pecas[computador]))

        tabela = ((0, 1, -1), (-1, 0, 1), (1, -1, 0))
        jogada = tabela[computador][jogador]

        if jogada == 0:
            resultado = "Deu empate, vocês escolheram a mesma peça."
        elif jogada == 1:
            resultado = 'Você ganhou. Parabéns!'
        else:
            resultado = 'O computador ganhou.'

    print(resultado)
    opcao = input('Jogar novamente? Pressione S (sim) para jogar novamente: ')
    system('cls') if(name == 'nt') else system('clear')
    print('resultado do jogo')
    print('Quantidade de jogadas: ', contadorJogadas)
    print(f'Você ganhou {contadorJogador} jogadas.')
    print(f'Você perdeu {contadorComputador} jogadas')