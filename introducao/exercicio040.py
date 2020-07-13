"""
EXERCÍCIO 040: Aquele Clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""


def main():

    try:
        primeira_nota = float(input('Digite a primeira nota: ').replace(',','.'))
        segunda_nota = float(input('Digite a segunda nota: ').replace(',','.'))

        if primeira_nota >= 0.0 and segunda_nota >= 0.0:
            media = (primeira_nota + segunda_nota)/2.0

            if media < 5.0:
                print('Media abaixo de 5.0: REPROVADO')
            elif media >= 7.0:
                print('Media 7.0 ou superior: APROVADO')
            else:
                print('Media entre 5.0 e 6.9: RECUPERAÇÃO')
        else:
            raise ValueError
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
