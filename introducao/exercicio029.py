"""
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""


def main():
    velocidade = input('Digite a velocidade do carro em km/h: ')

    try:
        velocidade_num = int(velocidade)

        if velocidade_num > 0:
            if velocidade_num > 80:
                print(f'Velocidade acima do limite. Multa de {(velocidade_num - 80)*7} reais.')
            else:
                print('Velocidade aceita.')
        else:
            raise ValueError

    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
