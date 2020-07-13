"""
EXERCÍCIO 054: Grupo de Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date


def main():

    try:
        maiores = 0
        for i in range(7):
            idade = date.today().year - int(input('Digite o ano de nascimento: '))
            if 0 <= idade <= 120:
                if idade >= 18:
                    maiores += 1
            else:
                raise ValueError

        print(f'Pessoas maiores de idade: {maiores}\n'
              f'Pessoas que nao sao maiores de idade: {7-maiores}')

    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
