"""
EXERCÍCIO 074: Maior e Menor Valores em Tupla

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""

from random import randint

def main():
    t = randint(-32767, 32767), randint(-32767, 32767), randint(-32767, 32767),\
        randint(-32767, 32767), randint(-32767, 32767)

    print('-='*50)
    print('Numeros gerados: ')
    print(t)

    print(f'Maior: {max(t)} \nMenor: {min(t)}')


if __name__ == '__main__':
    main()
