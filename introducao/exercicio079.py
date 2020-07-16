"""
EXERCÍCIO 079: Valores Únicos em uma Lista

Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""



def main():
    numeros = []

    try:
        leitura = ''
        while leitura != 'P':
            num = int(input('Digite um numero: '))
            if not num in numeros:
                numeros.append(num)
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        numeros = sorted(numeros)
        print('Numeros ordenados: ')
        print(numeros )

    except ValueError:
       print('Dado invalido.')





if __name__ == '__main__':
    main()
