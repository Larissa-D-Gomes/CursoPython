"""
EXERCÍCIO 050: Soma dos Pares

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

def main():
    valores = []
    try:
        for i in range(6):
            valores.append(int(input(f'Digite o valor [{i+1}]: ')))
        soma = 0

        for x in valores:
            if x % 2 == 0:
                soma += x
        print('A soma dos valores pares inseridos eh: ', soma)

    except ValueError:
        print('Dado invalido')

if __name__ == '__main__':
    main()
