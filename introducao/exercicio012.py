"""
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""






def main():

    preco = input('Digite o preco do produto: ')
    preco  = preco.replace(",",".")

    try:
        print(f'O preco do produto com 5% de desconto eh: {float(preco)*95/100} reais.')
    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
