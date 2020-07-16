"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0

Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

def main():
    try:
        n = int(input('Digite quantos n da sequencia de Fibonacci termos o programa mostrara: '))
        if n <= 0:
            raise ValueError

        print('0', end=" → ")
        n1 = 0
        n2 = 1
        for x in range (n-2):
            n1 += n2
            n2 = n1 - n2

            print(n1, end=" → ")

        n1 += n2

        print(n1)


    except ValueError:
        print('Dados invalido.')


if __name__ == '__main__':
    main()
