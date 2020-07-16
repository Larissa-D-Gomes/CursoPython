"""
EXERCÍCIO 067: Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

def main():

    try:
        num = int(input('Digite um numero positivo (negativo finaliza o programa): '))

        while num >= 0:
            print(f'A tabuada do {num} eh:')
            for x in range(11):
                print(f'{num} x {x} = {num*x}')

            num = int(input('Digite um numero positivo (negativo finaliza o programa): '))

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
