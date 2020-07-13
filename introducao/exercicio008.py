"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""






def main():
    pass
    medida = input('Digite a medida em metros: ')

    try:
        print( f'{float(medida)} m \n{float(medida)*100} cm \n{float(medida)*1000} mm' )
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
