"""
EXERCÍCIO 059: Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:

[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

def main():
    operacao = 0

    try:
        primeiro = float(input('Digite o primeiro valor: ').replace(',', '.'))
        segundo = float(input('Digite o segundo valor: ').replace(',', '.'))

        while operacao != '5':
            operacao = input('Digite a operacao desejada:\n'
                             '[ 1 ] Somar \n[ 2 ] Multiplicar \n[ 3 ] Maior'
                             '\n[ 4 ] Novos Numeros \n[ 5 ] Sair do programa\n')
            if operacao == '1':
                print(f'{primeiro} + {segundo} = {primeiro+segundo}')
            elif operacao == '2':
                print(f'{primeiro} * {segundo} = {primeiro*segundo}')
            elif operacao == '3':
                if primeiro > segundo:
                    print(f'{primeiro} > {segundo}')
                elif segundo > primeiro:
                    print(f'{segundo} > {primeiro}')
                else:
                    print(f'{primeiro} = {segundo}')
            elif operacao == '4':
                primeiro = float(input('Digite o primeiro valor: ').replace(',', '.'))
                segundo = float(input('Digite o segundo valor: ').replace(',', '.'))

            elif operacao != '5':
                print('Operacao invalida, tente outra.')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
