from os import system, name
import random

opcao = 's'

while opcao.upper() == 'S':
    system('cls') if name == 'nt' else system('clear')
    
    computador = random.randint(0, 2)
    jogador = int(input('''Escolha a opção para jogar:
        [0] Pedra
        [1] Papel
        [2] Tesoura
        Digite sua escolha: '''))
        
    pecas = ("Pedra", "Papel", "Tesoura")
    
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

    