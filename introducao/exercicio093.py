"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol

Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato.
"""


def main():
    try:
        jogador = {}
        jogador['Nome'] = input('Digite o nome do jogador: ')
        jogador['Partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
        jogador['Gols'] = 0
        for i in range(jogador['Partidas']):
            jogador['Gols'] += int(input(f'Digite quantos gols foram feitos'\
                                        f'na partida {i+1}: '))
        print(f'Nome do jogador: {jogador["Nome"]}'
              f'\nPartidas jogadas: {jogador["Partidas"]}'
              f'\nTotal de gols: {jogador["Gols"]}')
    except ValueError:
        print('Dado invalido.')
if __name__ == '__main__':
    main()
