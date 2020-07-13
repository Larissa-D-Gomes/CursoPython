"""
EXERCÍCIO 053: Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""


def main():
    frase = input('Digite a frase: ').replace(' ', '')

    if frase == frase[::-1]:
        print('Eh palindromo.')
    else:
        print('Nao eh palindromo.')


if __name__ == '__main__':
    main()
