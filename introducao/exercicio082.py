"""
EXERCÍCIO 082: Dividindo Valores em Várias Listas

Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
cria duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""



def main():
    try:
        lista = []
        leitura = ''
        while leitura != 'P':
            lista.append(int(input('Digite um numero: ')))
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        pares = []
        impares = []
        for x in lista:
            if x % 2 == 0:
                pares.append(x)
            else:
                impares.append(x)
        print('-='*15)
        print(f'TODOS VALORES \n{lista}')
        print('-='*15)
        print(f'PARES \n{pares}')
        print('-='*15)
        print(f'IMPARES \n{impares}')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
