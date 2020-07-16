"""
EXERCÍCIO 078: Maior e Menor Valores na Lista

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""


def main():
    numeros = []

    try:
        for i in range(1,6):
            numeros.append(int(input(f'Digite o numero [ {i} ]: ')))

        aux = max(numeros)
        print(f'\nO maior numero foi {aux} na posicao {numeros.index(aux)}.')
        aux = min(numeros)
        print(f'O menor numero foi {aux} na posicao {numeros.index(aux)}.')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
