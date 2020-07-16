"""
EXERCÍCIO 076: Lista de Preços com Tupla

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

def main():
    t = 'Televisao', 2300.0, 'Mouse', 120.50, 'Teclado', 327.95, 'Headset', 569.99,\
        'Playstation 4', 3000.0, 'Camera', 329.75, 'Blu-Ray', 900.50, 'Cadeira Gamer',\
        745.80, 'XBOX ONE', 2700.0

    for i in range(0, len(t)):
        if i % 2 == 0:
            print(f'{t[i]:.<35}', end="")
        else:
            print(f'R${t[i]}')


if __name__ == '__main__':
    main()
