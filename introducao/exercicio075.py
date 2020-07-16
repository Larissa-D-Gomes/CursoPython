"""
EXERCÍCIO 075: Análise de Dados em uma Tupla

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

def main():
    try:
        t = int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')), \
            int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: '))

        print(f'O valor 9 apareceu {t.count(9)} vez(es).')
        print(f'O valor 3 apareceu na posicao {t.index(3)} pela primeira vez.')

        pares = 0
        for i in t:
            if i % 2 == 0: pares+=1

        print(f'A quantidade de pares eh: {pares}')


    except ValueError:
        print('Dado invalido.')

if __name__ == '__main__':
    main()
