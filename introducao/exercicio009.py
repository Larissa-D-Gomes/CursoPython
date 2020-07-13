"""
EXERCÍCIO 009: Tabuada

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""






def main():
    pass
    entrada = input('Digite um numero: ')

    try:
        num = int(entrada)
        print(f'A tabuada do {num} eh:')
        for x in range(11):
            print(f'{num} x {x} = {num*x}')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
