"""
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere U$ 1,00 = R$ 5,30
"""






def main():
    pass
    dinheiro = input('Digite a quantidade de reais: ')

    dinheiro = dinheiro.replace(",",".")
    try:
        print(f'Voce pode comprar {float(dinheiro)/5.30} dolares.')
    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
