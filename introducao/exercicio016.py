"""
EXERCÍCIO 016: Quebrando um Número

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""



def main():
    numero = input('Digite o numero real: ')
    numero = numero.replace(",", ".")

    try:
        ind = numero.index('.')
        inteiro = numero[0:ind]
        print(f'Parte inteira: {inteiro}')
    except ValueError:
        try:
            print(f'Parte inteira: {int(numero)}')
        except ValueError:
            print('Dado invalido.')


if __name__ == '__main__':
    main()
