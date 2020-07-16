"""
EXERCÍCIO 057: Validação de Dados

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""


def main():
    leitura = input('Digite o sexo [M/F]: ')

    while leitura != 'M' and leitura != 'F':
        leitura = input('Dado invalido. Digite o sexo [M/F]: ')

    print('Valor aceito.')


if __name__ == '__main__':
    main()
