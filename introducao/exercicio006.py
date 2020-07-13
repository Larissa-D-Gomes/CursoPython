"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""






def main():
    pass
    leitura = input('Digite um numero: ')

    try:
        print( f'Dobro: {int(leitura)*2}\nTriplo: {int(leitura)*3} \nRaiz quadrada: {float(leitura)**(1/2)}' )
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
