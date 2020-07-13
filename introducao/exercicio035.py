"""
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""


def teste_lados(l1, l2, l3):
    return (abs(l2 - l3) < l1 < l2 + l3)

def main():

    try:
        l1 = float(input('Digite o primeiro lado do triangulo: '))
        l2 = float(input('Digite o segundo lado do triangulo: '))
        l3 = float(input('Digite o terceiro lado do triangulo: '))

        if l1 > 0 and l2 > 0 and l3 > 0:
            if teste_lados(l1, l2, l3) and teste_lados(l2, l1, l3) and teste_lados(l3, l2, l1):
                print('O triangulo existe.')
            else:
                print('O triangulo nao existe.')
        else:
            raise ValueError

    except ValueError:
        print('Dado(s) invalido(s).')


if __name__ == '__main__':
    main()
