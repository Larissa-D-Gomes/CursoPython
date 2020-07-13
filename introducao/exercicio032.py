"""
EXERCÍCIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""






def main():
    leitura = input('Digite o ano: ')

    try:
        ano = int(leitura)

        if ano % 4 == 0:
            print('Bissexto.')
        else:
            print('Nao Bissexto')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
