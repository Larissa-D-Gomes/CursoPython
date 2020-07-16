"""
EXERCÍCIO 077: Contando Vogais em Tupla

Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""






def main():
    t = 'Crie', 'um', 'programa', 'que', 'tenha', 'uma', 'tupla', 'varias',\
        'palavras', 'nao', 'usar', 'acentos', 'Depois', 'disso', 'voce', \
        'deve', 'mostrar', 'para', 'cada', 'palavra', 'quais', 'sao', \
        'as', 'suas', 'vogais'

    for i in t:
        maiuscula = i.upper()
        print(f'\n{i}: ', end='')

        for j in maiuscula:
            if j in 'AEIOU':
                print(j, end=' ')

if __name__ == '__main__':
    main()
