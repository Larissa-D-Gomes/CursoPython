"""
EXERCÍCIO 080: Lista Ordenada sem Repetições

Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

def main():
    numeros = []
    inseriu = False
    j = 0
    try:
        numeros.append(int(input('Digite o numero: ')))
        for i in range(4):
            l = len(numeros)
            num = int(input('Digite o numero: '))
            if num > numeros[l-1]:
                numeros.append(num)
            else:
                while not inseriu and j < l:
                    if num < numeros[j]:
                        numeros.insert(j, num)
                        inseriu = True
                    j+=1
                j = 0
                inseriu = False

        print(numeros)

    except ValueError:
       print('Dado invalido.')


if __name__ == '__main__':
    main()
