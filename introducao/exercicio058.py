"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

from random import randint

def main():
    sorteado = randint(0,10)
    tentativas = 1

    while int(input('Digite um numero entre 0 e 10: ')) != sorteado:
        print('Voce errou! Tente novamente.', sorteado)
        tentativas+=1

    print(f'Voce acertou! E precisou de {tentativas} tentativas')


if __name__ == '__main__':
    main()
