"""
EXERCÍCIO 090: Dicionário em Python

Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""



def main():
    try:
        aluno = {}
        aluno['Nome'] = input('Digite o nome do aluno: ')
        aluno['Media'] = float(input('Digite a media do aluno: '))

        if aluno['Media'] < 0.0:
            raise ValueError
        if aluno['Media'] < 6.0:
            aluno['Situacao'] = 'REPROVADO'
        else:
            aluno['Situacao'] = 'APROVADO'

        for i, j in aluno.items():
            print(f'{i}: {j}')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
