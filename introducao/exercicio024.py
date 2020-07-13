"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""






def main():
    cidade = input('Digite o nome da cidade: ')
    print("O nome da cidade comeca com 'Santo'?",cidade.split(" ", 1)[0].upper() == 'SANTO')


if __name__ == '__main__':
    main()
