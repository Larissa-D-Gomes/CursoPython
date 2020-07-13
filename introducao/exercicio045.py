"""
EXERCÍCIO 045: Pedra, Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint

def cod_jogada(x):
    if x == 1:
        jogada = 'Pedra'
    elif x == 2:
        jogada = 'Papel'
    else:
        jogada = 'Tesoura'

    return jogada

def decidir_ganhador(jogador, computador):
    if jogador == 1 and computador == 3:
        resp = 'jogador'
    elif jogador == 3 and computador == 1:
        resp = 'computador'
    elif jogador == 1 and computador == 2:
        resp = 'computador'
    elif jogador == 2 and computador == 1:
        resp = 'jogador'
    elif jogador == 3 and computador == 2:
        resp = 'jogador'
    else:
        resp = 'computador'

    return resp

def main():
    try:
        jogador = int(input('[1] - Pedra \n[2] - Papel \n[3] - Tesoura \nEscolha a sua jogada: '))

        if 0 < jogador < 4:
            computador = randint(1,4)

            if computador == jogador:
                print(f'Empate: ambos jogaram {cod_jogada(computador)}')
            else:
                print(f'O vencedor foi o {decidir_ganhador(jogador, computador)}\n'
                      f'Jogador: {cod_jogada(jogador)}\n'
                      f'Computador: {cod_jogada(computador)}')

        else:
            raise ValueError
    except ValueError:
        print('Jogada invalida.')



if __name__ == '__main__':
    main()
