"""
EXERCÍCIO 068: Jogo do Par ou Ímpar

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

def main():
    try:
        vitoria = True
        cont = 0

        while vitoria:
            p_ou_i = input('[ 1 ] Jogar com IMPAR \n[ 2 ] Jogar com PAR\n')

            if p_ou_i != '1' and p_ou_i != '2':
                raise ValueError

            jogador = int(input('Digite seu numero: '))
            computador = randint(0, 9999)

            print(f'Jogador: {jogador} \nComputador: {computador}')

            result = ( jogador + computador) % 2

            if p_ou_i == '1':
                if result == 1:
                    cont+=1
                else:
                    vitoria = False
            else:
                if result == 0:
                    cont+=1
                else:
                    vitoria = False

        print(f'O jogador ganhou {cont} partidas consecutivas')
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
