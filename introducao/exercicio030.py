"""
EXERCÍCIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""



def main():
    leitura = input('Digite um numero inteiro: ')

    try:
        numero = int(leitura)

        if numero % 2 == 0:
            print(f'{numero} eh par.')
        else:
            print(f'{numero} eh impar.')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
