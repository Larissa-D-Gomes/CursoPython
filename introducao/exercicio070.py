"""
EXERCÍCIO 070: Estatísticas em Produtos

Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""

from produto import Produto


def main():

    try:
        total = 0
        maiores_mil = 0
        mais_barato = None
        produtos = []
        leitura = ''
        i = 0

        while leitura != 'P':
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o preco do produto: ').replace(',', '.'))
            produtos.append(Produto(nome, preco))
            total += produtos[i].getPreco()

            if produtos[i].getPreco() > 1000:
                maiores_mil += 1

            if mais_barato == None:
                mais_barato = produtos[i]
            elif preco < mais_barato.getPreco():
                mais_barato = produtos[i]

            leitura = input('Se deseja continura insira qualquer tecla.\n' \
                        'Se deseja parar o programa insira [P/p]: ').upper()
            i+=1

        print(f'\nTotal gasto: {total} \nQuantos produtos custam mais que 1000:'
              f' {maiores_mil} \nProduto mais barato: {mais_barato.getNome()}')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
