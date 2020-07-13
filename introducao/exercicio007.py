"""
EXERCÍCIO 007: Média Aritmética

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""






def main():
    pass
    primeira = input('Digite a primeira nota: ')
    segunda = input('Digite a segunda nota: ')

    try:
        print( f'Sua media eh: {(float(primeira)+float(segunda))/2}' )
    except ValueError:
        print('Dado(s) invalido(s).')

if __name__ == '__main__':
    main()
