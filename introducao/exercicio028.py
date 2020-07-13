"""
EXERCÍCIO 028: Jogo da Adivinhação v1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

def main():
    sorteado = randint(0,5)
    numero = input('Digite um numero entre 0 e 5: ')

    if numero == sorteado:
        print('Voce venceu.')
    else:
        print('Voce perdeu.')


if __name__ == '__main__':
    main()
