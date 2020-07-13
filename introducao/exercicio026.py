"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""



def main():
    frase = input('Digite a frase: ').upper()

    print(f"A letra 'A' aparece {frase.count('A')} vez(es) na frase.")
    try:
        print(f"A letra 'A' aparece a primeira vez na posicao {frase.index('A')}."
              f"\nA letra 'A' aparece pela ultima vez na posicao {len(frase) - 1 - frase[::-1].index('A')}.")
    except ValueError:
        print("A letra 'A' nao aparece na frase.")

if __name__ == '__main__':
    main()
