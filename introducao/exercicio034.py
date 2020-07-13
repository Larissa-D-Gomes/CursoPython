"""
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""



def main():
        leitura = input('Digite o salario: ')

        try:
            salario = float(leitura)
            if salario > 0:
                if salario > 1250.0:
                    input(f'Sua salario de {salario} ira para {salario*110.0/100.0}, com 10% de aumento')
                else:
                    input(f'Sua salario de {salario} ira para {salario*115.0/100.0}, com 10% de aumento')
            else:
                raise ValueError

        except ValueError:
            print('Dado invalido.')


if __name__ == '__main__':
    main()
