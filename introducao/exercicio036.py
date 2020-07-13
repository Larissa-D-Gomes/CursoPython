"""
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""


def main():
    try:
        valor = int(input('Digite o valor da casa: '))
        salario = int(input('Digite o salario do comprador: '))
        anos = int(input('Digite em quantos ano ira pagar: '))

        if valor > 0 and salario > 0 and anos > 0:
            prestacao_mensal = valor / (anos * 12)
            if prestacao_mensal > (salario*30/100):
                print('Emprestimo negado.')
            else:
                print('Emprestimo aprovado.')
        else:
            raise Exception
    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
