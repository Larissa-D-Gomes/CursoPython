"""
EXERCÍCIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""






def main():
    numeros = []

    try:
        numeros.append(int(input('Digite o primeiro numero: ')))
        numeros.append(int(input('Digite o segundo numero: ')))
        numeros.append(int(input('Digite o terceiro numero: ')))

        maior = numeros[0]
        menor = numeros[0]

        for x in range(1,3):
            if numeros[x] < menor:
                menor = numeros[x]
            if numeros[x] > maior:
                maior = numeros[x]

        print(f'O maior numero eh: {maior} \nO menor numero eh: {menor}')


    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
