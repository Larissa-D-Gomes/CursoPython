"""
EXERCÍCIO 023: Separando Dígitos de um Número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""

def main():
    numero = input('Digite o numero: ')

    try:
        inteiro = int(numero)
        milhar  = inteiro//1000
        centena = (inteiro - (milhar * 1000) )//100
        dezena  = (inteiro - (centena * 100) - (milhar * 1000) )//10
        unidade  = inteiro - (dezena * 10) - (centena * 100) - (milhar * 1000)

        print(f'Unidade: {unidade} \nDezena: {dezena} \n'
              f'Centena: {centena} \nMilhar: {milhar}')


    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
