"""
EXERCÍCIO 060: Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

from math import factorial

def main():
    try:
        numero = int(input('Digite um numero inteiro para calcular seu fatorial: '))
        print(f'{numero}! = ')
        for x in range(numero, 1, -1):
            print(f'{x} x', end=" ")
        print(f'{x} = {factorial(numero)}')
    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
