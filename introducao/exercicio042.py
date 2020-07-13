"""
EXERCÍCIO 042: Analisando Triângulos v2.0

Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
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
                print('\nO triangulo existe.')

                if l1 == l2 and l2 == l3:
                    print('Equilatero: todos os lados iguais.')
                elif l1 == l2 or l2 == l3 or l1 == l3:
                    print('Isoceles: dois lados iguais.')
                else:
                    print('Escaleno: todos os lados diferentes.')
            else:
                print('O triangulo nao existe.')
        else:
            raise ValueError

    except ValueError:
        print('Dado(s) invalido(s).')


if __name__ == '__main__':
    main()