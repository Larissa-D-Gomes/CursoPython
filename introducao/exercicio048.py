"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""


def main():
    soma = 0

    for i in range(1, 500, 2):
        if i % 3 == 0:
            soma += i

    print('A soma eh:', soma)


if __name__ == '__main__':
    main()
