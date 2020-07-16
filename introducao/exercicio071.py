"""
EXERCÍCIO 071: Simulador de Caixa Eletrônico

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""

def calculo(nota, valor):
    quant = valor // nota
    if quant > 0:
        print(f'[ {quant} ] Notas de {nota}.')

    return valor - (nota * quant)

def main():
    try:
        valor = int(input('Digite o valor que deseja sacar: '))

        if valor < 0:
            raise ValueError

        valor = calculo(50, valor)
        valor = calculo(20, valor)
        valor = calculo(10, valor)
        valor = calculo(1, valor)

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
