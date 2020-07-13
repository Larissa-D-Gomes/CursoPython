"""
EXERCÍCIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math


def main():
    angulo = input('Digite o angulo: ')

    try:
        print(f'Seno: {math.sin(float(angulo))} \nCosseno: {math.cos(float(angulo))}\n '
              f'Tangemte: {math.tan(float(angulo))}')
    except ValueError:
        print('Dado(s) invalido(s).')

if __name__ == '__main__':
    main()
