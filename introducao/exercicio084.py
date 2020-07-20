"""
EXERCÍCIO 084: Lista Composta e Análise de Dados

Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

def main():
    try:
        aux = []
        lista = []
        aux.append(input('Digite o nome: '))
        peso = float(input('Digite o peso: '))
        if peso < 0.0:
            raise ValueError
        aux.append(peso)
        lista.append(aux[:])
        aux.clear()
        leitura = input('Insira qualquer tecla para continuar.\n'
                        'Digite [P/p] para para o programa: ').upper()
        maior = menor = lista[0][1]

        while leitura != 'P':
            aux.append(input('Digite o nome: '))
            peso = float(input('Digite o peso: '))
            if peso < 0.0:
                raise ValueError
            aux.append(peso)
            lista.append(aux[:])
            aux.clear()
            if peso > maior:
                maior = peso
            elif peso < menor:
                menor = peso
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        print(f'Foram cadastradas {len(lista)} pessoas.')
        for i in lista:
            if i[1] == maior:
                print(f'{i[0]} eh uma pessoa com maior peso.')
        for i in lista:
            if i[1] == menor:
                print(f'{i[0]} eh uma pessoa com menor peso.')


    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
