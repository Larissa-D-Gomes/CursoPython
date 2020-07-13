"""
EXERCÍCIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""






def main():
    salario = input('Digite o salario atual: ')
    salario  = salario.replace(",",".")

    try:
        print(f'O salario com 15% de aumento eh: {float(salario)*115/100} reais.')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
