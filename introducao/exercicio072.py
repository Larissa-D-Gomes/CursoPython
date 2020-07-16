"""
EXERCÍCIO 072: Número por Extenso

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""



def main():
    tup = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',\
          'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',\
          'dezoito', 'dezenove', 'vinte'

    print('Programa para mostrar inteiros de 0-20 por extenso.')

    try:
        posicao = int(input('Digite o numero que deseja ver por extenso [0:20]: '))

        if not(0 <= posicao <= 20):
            raise ValueError

        print(f'{posicao} por extenso = {tup[posicao]}')

    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
