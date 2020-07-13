"""
EXERCÍCIO 005: Antecessor e Sucessor

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""


def main():
    pass
    leitura = input('Digite um numero inteiro: ')

    try:
        print('Antecessor:', int(leitura)-1,'\nSucessor:',int(leitura)+1 )
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
