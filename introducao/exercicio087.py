"""
EXERCÍCIO 087: Mais Sobre Matriz em Python

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""

def main():
    try:
        matriz = [[0,0,0],[0,0,0],[0,0,0]]

        for i in range(3):
            for j in range(3):
                matriz[i][j] = int(input(f'Digite o valor [{i}][{j}]: '))

        print('==== PRINT MATRIZ ====')
        for i in matriz:
            for j in i:
                print(f'[{j}]', end=' ')
            print('')

        print('==== SOMA PARES ====')
        soma = 0
        for i in matriz:
            for j in i:
                if j % 2 == 0:
                    soma += j
        print(f'Soma dos valores pares: {soma}')

        print('==== SOMA VALORES TERCEIRA COLUNA ====')
        soma = 0
        for i in range(3):
            soma += matriz[i][2]

        print(f'Soma da terceira coluna: {soma}')

        print('==== MAIOR VALOR SEGUNDA LINHA ====')
        maior = matriz[1][0]
        for i in range(1, 3):
            if matriz[1][i] > maior:
                maior = matriz[1][i]

        print(f'Maior valor segunda linha: {maior}')
    except ValueError:
        print('Dado invalido')



if __name__ == '__main__':
    main()
