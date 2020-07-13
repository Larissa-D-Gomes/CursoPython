"""
EXERCÍCIO 019: Sorteando um Item na Lista

Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

import random

def main():
    alunos = []
    print('Nomes com caracteres nao alfabeticos irao interroper a execucao.')
    leitura = input('Digite o nome: ')

    while leitura.isalpha():
        alunos.append(leitura)
        leitura = input('Digite o nome: ')

    try:
        print(random.choice(alunos))
    except IndexError:
        print('Lista vazia.')

if __name__ == '__main__':
    main()
