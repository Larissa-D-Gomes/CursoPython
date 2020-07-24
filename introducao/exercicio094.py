"""
EXERCÍCIO 094: Unindo Dicionários e Listas

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:

A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""


def main():
    try:
        lista = []
        leitura = ''
        soma_idade = 0
        while leitura != 'P':
            pessoa = {}
            pessoa['Nome'] = input('Digite o nome: ')
            pessoa['Sexo'] = input('Digite o sexo [M/F]: ').upper()
            if pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
                raise ValueError
            pessoa['Idade'] = int(input('Digite a idade: '))
            soma_idade += pessoa['Idade']
            lista.append(pessoa)
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        print(f'Foram cadastradas {len(lista)} pessoas.')
        media = soma_idade / len(lista)
        print(f'Media de idade: {media}')
        acima_media = []
        mulheres = []
        for i in lista:
            if i['Sexo'] == 'F':
                mulheres.append(i.copy())
            if i['Idade'] > media:
                acima_media.append(i.copy())

        print('==== PESSOAS ====')
        for i in lista:
            for k, j in i.items():
                print(f'{k}: {j}')
            print('')

        print('==== MULHERES ====')
        for i in mulheres:
            for k, j in i.items():
                print(f'{k}: {j}')
            print('')


        print('==== ACIMA DA MEDIA DE IDADES ====')
        for i in acima_media:
            for k, j in i.items():
                print(f'{k}: {j}')
            print('')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
