"""
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""




def main():
    leitura = input('Digite a distancia da viagem em km: ')

    try:
        distancia = float(leitura)

        if distancia > 0.0:

            if distancia < 200.0:
                print(f'O valor da viagem eh {distancia*0.50} reais.')
            else:
                print(f'O valor da viagem eh {distancia*0.45} reais.')


        else:
            raise ValueError

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
