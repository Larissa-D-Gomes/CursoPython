"""
EXERCÍCIO 061: Progressão Aritmética v2.0

Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""




def main():
    def main():
        try:
            num = float(input('Digite o primeiro termo da PA: '))
            razao = float(input('Digite a razao da PA: '))
            i = 0
            while i < 10:
                i += 1
                print(f'[{i}] - {num}')
                num += razao

        except ValueError:
            print('Dado invalido.')



if __name__ == '__main__':
    main()
