"""
EXERCÍCIO 089: Boletim com Listas Compostas

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma
lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
"""


def main():
    try:
        boletim = []
        aux = []
        leitura = ''
        while leitura != 'P':
            aux.append(input('Digite o nome do aluno: '))
            nota1 = float(input('Digite a primeira nota do aluno: '))
            nota2 = float(input('Digite a segunda nota do aluno: '))
            if nota1 < 0.0 or nota2 < 0.0:
                raise ValueError

            aux.append(nota1)
            aux.append(nota2)
            aux.append((nota1+nota2)/2.0)

            boletim.append(aux[:])
            aux.clear()
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        for i in boletim:
            print(f'Nome: {i[0]}\n'
                  f'Primeira nota: {i[1]}\n'
                  f'Segunda nota: {i[2]}\n'
                  f'Media: {i[3]}\n')
        leitura = ''
        achou = False

        while leitura != 'P':
            nome = input('Digite o nome do aluno que deseja pesquisar: ')
            for i in boletim:
                if nome in i:
                    print(f'Nome: {i[0]}\n'
                          f'Primeira nota: {i[1]}\n'
                          f'Segunda nota: {i[2]}\n'
                          f'Media: {i[3]}\n')
                    achou = True
                    break
            if achou == True:
                achou = False
            else:
                print('Aluna(o) nao encontrado.')

            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
