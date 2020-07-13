"""
EXERCÍCIO 041: Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

def main():
    try:
        idade = date.today().year - int(input('Digite o ano de nascimento: '))

        if 0 <= idade <= 120:
            if idade <= 9:
                print('MIRIM')
            elif idade <= 14:
                print('INFANTIL')
            elif idade <= 19:
                print('JUNIOR')
            elif idade <= 25:
                print('SENIOR')
            else:
                print('Master')
        else:
            raise ValueError
    except ValueError:
        input('Dado invalido.')


if __name__ == '__main__':
    main()
