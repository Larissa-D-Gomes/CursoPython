"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

def main():

    try:
        idade = date.today().year - int(input('Digite o ano de nascimento: '))

        if 0 <= idade <= 120:
            if idade == 18:
                print('Ja esta na hora de se alistar.')
            elif idade < 18:
                print(f'Ainda vai se alistar e faltam {18-idade} ano(s).')
            else:
                print(f'Ja passou do prazo para o alistamento em {idade-18} ano(s).')
        else:
            raise ValueError
    except ValueError:
        input('Dado invalido.')

if __name__ == '__main__':
    main()
