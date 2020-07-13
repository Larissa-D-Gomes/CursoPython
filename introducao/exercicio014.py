"""
EXERCÍCIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""






def main():
    temperatura = input('Digite a temperatura em ºC: ')
    temperatura = temperatura.replace(",", ".")

    try:
        print(f'{(float(temperatura) * 9 / 5) + 32} ºF')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
