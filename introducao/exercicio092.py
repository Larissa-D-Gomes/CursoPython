"""
EXERCÍCIO 092: Cadastro de Trabalhador em Python

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime

def main():
    try:
        cadastro = {}
        cadastro['Nome'] = input('Digite o nome: ')
        cadastro['Idade'] = datetime.now().year - int(input('Digite o ano de nascimento: '))
        if cadastro['Idade'] < 0:
            raise ValueError
        cadastro['Carteira'] = int(input('Digite a carteira de trabalho,'
                                         ' se nao tiver insira 0: '))
        if cadastro['Carteira'] != 0:
            cadastro['Contratacao'] = int(input('Digite o ano de contratacao: '))
            if cadastro['Contratacao'] < 1930:
                raise ValueError
            cadastro['Salario'] = float(input('Digite o salario: '))
            if cadastro['Salario'] <= 0.0:
                raise ValueError
            cadastro['Aposentadoria'] = cadastro['Idade'] + cadastro['Contratacao'] + \
                                        + 35 - datetime.now().year
        for i, j in cadastro:
            print(f'{i}: {j}')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
