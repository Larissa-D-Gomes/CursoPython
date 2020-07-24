"""
EXERCÍCIO 095: Aprimorando os Dicionários

Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""


def main():
    try:
        lista = []
        leitura = ''
        while leitura != 'P':
            jogador = {}
            jogador['Nome'] = input('Digite o nome do jogador: ')
            jogador['Partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
            jogador['Gols'] = 0
            for i in range(jogador['Partidas']):
                jogador['Gols'] += int(input(f'Digite quantos gols foram feitos' \
                                             f'na partida {i + 1}: '))
            lista.append(jogador)
            leitura = input('Insira qualquer tecla para continuar.\n'
                            'Digite [P/p] para para o programa: ').upper()

        for i in lista:
            print('='*20)
            for j, k in i.items():
                print(f'{j}: {k}')

        leitura = input('Insira o nome do jogador que deseja procurar.\n'
                        'Digite [P] para para o programa: ')
        achou = False
        while leitura != 'P':
            for i in lista:
                if i['Nome'] == leitura:
                    for j, k in i.items():
                        print(f'{j}: {k}')
                        achou = True
                    if achou:
                        break
            if not achou:
                print('Jogador nao encontrado.')
            else:
                achou = False

            leitura = input('Insira o nome do jogador que deseja procurar.\n'
                            'Digite [P] para para o programa: ')

    except ValueError:
        print('Dado invalido.')


if __name__ == '__main__':
    main()
