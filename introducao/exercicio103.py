"""
Fazer um programa ler palavras de um arquivo, uma por linha,
e contar quantas começam com a letra 'a' (ou 'A').
"""


def main():
    try:
        arq = open(input('Digite o nome do arquivo: '), 'rt')
        contador = 0
        for i in arq:
            contador += i.count(' a')
            contador += i.count(' A')
            if i[0] == 'A' or i[0] == 'a':
                contador += 1

        print(f"{contador} palavras comecam com a letra 'A'.")

        arq.close()
    except FileNotFoundError:
        print('O arquivo nao existe!')

if __name__ == '__main__':
    main()
