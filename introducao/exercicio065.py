"""
EXERCÍCIO 065: Maior e Menor Valores

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

def main():
    try:
        leitura = int(input('Digite um numero inteiro: '))
        maior = leitura
        menor = leitura
        leitura = input('Se deseja parar o programa digite [P]: ')

        while leitura != 'P':
            leitura = int(input('Digite um numero inteiro: '))

            if leitura > maior:
                maior = leitura
            elif leitura < menor:
                menor = leitura

            leitura = input('Se deseja parar o programa digite [P]: ')

        print(f'\nO maior numero foi: {maior} \nO menor numero foi: {menor}')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
