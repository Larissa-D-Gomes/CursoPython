"""
EXERCÍCIO 037: Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:

- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""


def main():
    try:
        numero = int(input('Digite um numero inteiro: '))
        conversao = int(input('Escolha a base da conversao: \n[1] Binario \n[2] Octal\n[3] Hexadecimal\n'))

        if 0 < conversao < 4:
            if conversao == 1:
                print(f'{numero}(10) = {bin(numero)}')
            elif conversao == 2:
                print(f'{numero}(10) = {oct(numero)}')
            else:
                print(f'{numero}(10) = {hex(numero)}')
        else:
            raise ValueError
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
