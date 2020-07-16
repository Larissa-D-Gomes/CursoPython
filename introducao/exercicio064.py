"""
EXERCÍCIO 064: Tratando Vários Valores v1.0

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""


def main():
    try:
        leitura = int(input('Digite um numero inteiro: '))
        quant = 0
        soma = 0
        while leitura != 999:
            quant += 1
            soma += leitura
            leitura = int(input('Digite um numero inteiro: '))

        print(f'\nForam digitados {quant} numeros. \nA soma foi: {soma}')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
