from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
tony_jogada = randint(0, 2)
print('''Escolha: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input(''))
print('''
jo
ken
pô!!''')
print('-='*11)
print('Você jogou: {}'.format(itens[jogador]))
print('Computador jogou: {}'.format(itens[tony_jogada]))
print('-='*11)
if tony_jogada == 0:

    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('VOCÊ GANHOU!')

    elif jogador == 2:
        print('COMPUTADOR GANHOU!')

elif tony_jogada == 1:

    if jogador == 0:

        print('COMPUTADOR GANHOU!')

    elif jogador == 1:

        print('EMPATE')

    elif jogador == 2:

        print('VOCÊ GANHOU!')

elif tony_jogada == 2:

    if jogador == 0:
        print('VOCÊ GANHOU!')

    elif jogador == 1:
        print('COMPUTADOR GANHOU!')

    elif jogador == 2:
        print('EMPATE')

input('Aperte enter para sair')