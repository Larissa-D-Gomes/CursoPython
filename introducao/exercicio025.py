"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""






def main():
    nome = input('Digite o nome: ')
    nomes = nome.split(" ")

    for x in nomes:
        resp = x.upper() == 'SILVA'
        if resp:
            break

    print("Existem 'Silva no nome?'", resp)


if __name__ == '__main__':
    main()
