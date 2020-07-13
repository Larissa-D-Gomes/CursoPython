"""
EXERCÍCIO 038: Comparando Números

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""


def main():
    try:
        valor_1 = int(input('Digite o primeiro valor: '))
        valor_2 = int(input('Digite o segundo valor: '))

        if valor_1 > valor_2:
            print('O primeiro valor eh maior.')
        elif valor_2 > valor_1:
            print('O segundo valor eh maior.')
        else:
            print('Nao existe valor maior, os dois sao iguais.')
    except ValueError:
        print('Dados invalido.')


if __name__ == '__main__':
    main()
