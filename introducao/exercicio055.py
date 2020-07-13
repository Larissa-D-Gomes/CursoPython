"""
EXERCÍCIO 055: Maior e Menor da Sequência

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""


def main():
    try:
        maior = menor = leitura = float(input('Digite o peso 1: '))
        if 0.0 < leitura < 500.0:
            for i in range(4):
                leitura = float(input(f'Digite o peso {i+2}: '))
                if 0.0 < leitura < 500.0:
                    if leitura > maior:
                        maior = leitura
                    elif leitura < menor:
                        menor = leitura
                else:
                    raise ValueError
            print(f'Maior peso: {maior} \nMenor peso: {menor}')
        else:
            raise ValueError

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
