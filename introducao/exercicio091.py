"""
EXERCÍCIO 091: Jogo de Dados em Python

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from operator import itemgetter
def main():
    jogadas = {}
    for i in range(4):
        input('INSIRA QUALQUER TECLA PARA JOGAR O DADO.')
        jogadas[f'jogador{str(i+1)}'] = randint(1, 6)

    print('=== CLASSIFICACAO ===')
    for i, j in enumerate(sorted(jogadas.items(), key=itemgetter(1), reverse=True)):
        print(f'{j[0]}: {j[1]}')


if __name__ == '__main__':
    main()
