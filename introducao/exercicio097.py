"""
Fazer um programa para ler uma string de usuário e salvar em um arquivo .txt
"""


def main():
    leitura = input('Digite uma string: ')

    arq = open('arquivo.txt', 'wt')
    arq.write(leitura)
    arq.close()


if __name__ == '__main__':
    main()
