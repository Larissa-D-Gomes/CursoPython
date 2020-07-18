"""
EXERCÍCIO 081: Extraindo Dados de uma Lista

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

def main():
    try:
        lista = []
        leitura = ''
        while leitura != 'P':
            lista.append(int(input('Digite um numero: ')))
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        print(f'Foram digitados {len(lista)} numeros.')
        lista.sort(key = int, reverse= True)
        print(lista)

        if 5 in lista:
            print('O valor 5 esta na lista.')
        else:
            print('O valor 5 nao esta na lista.')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
