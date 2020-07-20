"""
EXERCÍCIO 088: Palpites Para a Mega Sena

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
jogo, cadastrando tudo em uma lista composta.
"""

from random import randint

def main():
    try:
        quant = int(input('Quantos jogos serao gerados: '))
        if quant < 0:
            raise ValueError
        lista = []
        aux = []

        for i in range(quant):
            j = 0
            while j < 6:
                num = randint(1,60)
                if num not in aux:
                    aux.append(num)
                    j+=1

            lista.append(aux[:])
            aux.clear()

        print(lista)
    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
