"""
EXERCÍCIO 046: Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep

def main():
    for i in range(10, 0, -1):
        print(i)
        sleep(1)
    print('*FOGOS DE ARTIFICIO*')

if __name__ == '__main__':
    main()
