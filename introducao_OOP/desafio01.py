"""

Você foi contratado para desenvolver um sistema de pesquisa de séries de televisão de um site.

O dono do site quer que você crie um programa desktop (sem conexão com a internet) para
que o usuário pesquise informações offline sobre séries de televisão.

As informações importantes sobre as séries são:

1) Nome da série
2) Ano de lançamento
3) Avaliação

O dono do site quer que o usuário possa digitar o nome da série, e o sistema deve
recuperar as informações sobre a série e mostrar na tela para o usuário.


EXEMPLO DE ENTRADA DO USUARIO
##########################################################################
'Breaking Bad'
##########################################################################


SAIDA NA TELA
##########################################################################
# A série Breaking Bad foi lançada no ano 2012 e possui avaliação de 9.4
##########################################################################

O site é https://www.imdb.com/chart/toptv

"""
import os

def separador(linha):
    return linha[linha.find('>')+1: linha.rfind('<')]

def leitura_arquivo():
    try:
        arq = open(os.path.join(os.getcwd(), 'series.html'), 'rt')
        series = []
        inicio_info = '<td class="titleColumn">'
        for i in arq:
            if inicio_info in i:
                arq.readline()
                nome = separador(arq.readline())
                ano = separador(arq.readline()).replace(')','').replace('(','')
                arq.readline()
                arq.readline()
                avaliacao = separador(arq.readline())
                print(avaliacao)

    except FileNotFoundError:
        print('ARQUIVO NAO ENCONTRADO')

def main():
    leitura_arquivo()



if __name__ == '__main__':
    main()
