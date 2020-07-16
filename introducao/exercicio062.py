"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0

Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""



def main():
    try:
        num = float(input('Digite o primeiro termo da PA: '))
        razao = float(input('Digite a razao da PA: '))
        i = 10
        while i > 0:
            for x in range(i):
                print(f'[{x}] - {num}')
                num += razao
            i = int(input('Deseja mostrar mais quantos termos? '))

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
