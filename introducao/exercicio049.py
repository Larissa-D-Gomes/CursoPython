"""
EXERCÍCIO 049: Tabuada v2.0

Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
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
