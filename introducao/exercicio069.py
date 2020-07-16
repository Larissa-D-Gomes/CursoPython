"""
EXERCÍCIO 069: Análise de Dados do Grupo

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""


def main():
    try:
        maiores = 0
        homens = 0
        menores = 0
        leitura = ''
        while leitura != 'N':
            idade = int(input('Digite a idade: '))

            if 0 >= idade or idade >= 120:
                raise ValueError

            sexo = input('Digite o sexo [F/M]: ').upper()

            if (sexo != 'M' and sexo != 'F'):
                raise ValueError

            if idade >= 18:
                maiores += 1

            if sexo == 'M':
                homens += 1
            elif idade < 20:
                menores += 1

            leitura = input('Se deseja continura insira qualquer tecla.\n'\
                       'Se deseja parar o programa insira [N/n]: ').upper()

        print(f'Maiores de 18 anos: {maiores} \nHomens: {homens} '
              f'\nMulheres menores de 20 anos: {menores}')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
