"""
EXERCÍCIO 085: Listas com Pares e Ímpares

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""






def main():
    try:
        lista = [[],[]]
        for x in range(7):
            valor = int(input('Digite o numero: '))
            if valor % 2 == 0:
                lista[0].append(valor)
            else:
                lista[1].append(valor)
        lista[0].sort()
        print(f'PARES: {lista[0]}')
        lista[1].sort()
        print(f'IMPARES: {lista[1]}')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()
