"""
EXERCÍCIO 086: Matriz em Python

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

No final, mostre a matriz na tela, com a formatação correta.
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
    except ValueError:
        print('Dado invalido')


if __name__ == '__main__':
    main()
