"""
EXERCÍCIO 015: Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""



def main():
    distancia = input('Digite a distancia percorrida em km: ')
    distancia = distancia.replace(",", ".")

    dias = input('Digite a quantidade de dias que o carro foi alugado: ')
    dias = dias.replace(",", ".")

    try:
        print(f'Preco final: {(float(distancia)*0.15) + (float(dias)*60)}')
    except ValueError:
        print('Dado invalido.')



if __name__ == '__main__':
    main()
