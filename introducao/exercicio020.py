"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista

O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

def main():
    alunos = []
    print('Nomes com caracteres nao alfabeticos irao interroper a execucao.')

    for x in range(4):
        leitura = input('Digite o nome: ')
        alunos.append(leitura)

    print('Ordem de apresentacao: ')
    for x in range(4):
        sorteado = random.choice(alunos)
        print(f'{x+1}- {sorteado}')
        alunos.remove(sorteado)


if __name__ == '__main__':
    main()
