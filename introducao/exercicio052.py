"""
EXERCÍCIO 052: Números Primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""


def main():
    try:
        numero = int(input('Digite um numero inteiro: '))

        has_div = numero == 1
        i = 2
        while not(has_div) and i < numero:
            has_div = (numero % i == 0)
            i+=1

        if has_div:
            print(f'O numero {numero} nao eh primo.')
        else:
            print(f'O numero {numero} eh primo.')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
