"""
EXERCÍCIO 051: Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

def main():
    try:
        num = float(input('Digite o primeiro termo da PA: '))
        razao = float(input('Digite a razao da PA: '))

        for i in range(10):
            print(f'[{i+1}] - {num}')
            num += razao

    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
