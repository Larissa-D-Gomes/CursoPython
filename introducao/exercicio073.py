"""
EXERCÍCIO 073: Tuplas com Times de Futebol

Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
"""

def main():
    tabela = 'Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR', 'Sao Paulo',\
             'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco da Gama',\
             'Atletico-MG', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA', \
             'Chapecoense', 'Avai'

    print('-='*15)
    print('5 PRIMEIROS: \n')
    for i in range(5):
        print(f'[ {i+1} ] {tabela[i]} ')

    print('-='*15)
    print('4 ULTIMOS: \n')
    for i in range(16,20):
        print(f'[ {i+1} ] {tabela[i]} ')

    print('-='*15)
    print('TIMES EM ORDEM ALFABETICA: \n')
    ordenada = sorted(tabela)
    for i in range(20):
        print(ordenada[i])

    print('-='*15)
    print(F'\nPOSICAO CHAPECOENSE: {tabela.index("Chapecoense")+1} \n')


if __name__ == '__main__':
    main()
