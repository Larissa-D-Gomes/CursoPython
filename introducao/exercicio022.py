"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

def main():
    nome = input('Digite o nome completo: ')
    print('Nome em letras maiusculas:', nome.upper())
    print('Nome em letras minusculas:',nome.lower())

    sem_espaco = nome.replace(' ', '')
    print('Quantidade de letras:', len(sem_espaco))

    primeiro_nome = nome[0:nome.index(' ')]
    print('Quantidade de letras primeiro nome:', len(primeiro_nome))




if __name__ == '__main__':
    main()
