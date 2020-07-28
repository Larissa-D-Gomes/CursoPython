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
from serie import Serie
from banco_de_dados import BancoDeDados
import os


#Funcao para separar informacao de tag
def separador(linha):
    return linha[linha.find('>')+1: linha.rfind('<')]

def leitura_arquivo():
    try:
        arq = open(os.path.join(os.getcwd(), 'series.html'), 'rt')
        inicio_info = '<td class="titleColumn">'#Tag de inicio de informacoes de serie
        series = {}
        for i in arq:
            if inicio_info in i:#Ler linhas de arquivo
                arq.readline()#Pular linha
                nome = separador(arq.readline())
                ano = separador(arq.readline()).replace(')','').replace('(','')
                arq.readline()#Pular linha
                arq.readline()#Pular linha
                avaliacao = separador(arq.readline())
                series[nome] = Serie(nome, ano, avaliacao)
    except FileNotFoundError:
        print('ARQUIVO NAO ENCONTRADO')
    return series

def main():

    series = leitura_arquivo()
    bd = BancoDeDados()
    bd.dados = series
    if not bd.salvar_dados():
        print('ERRO.')
    else:
        if bd.carregar_dados():
            leitura = ''
            while leitura != 'P':
                n = input('Digite o nome da serie que deseja pesquisar: ')
                aux = bd.buscar_serie(n)
                if aux == None:
                    print('Serie nao encontrada.')
                else:
                    print(aux)
                leitura = input('Insira qualquer tecla para continuar ou [P/p] para parar: ').upper()
        else:
            print('ERRO!')



if __name__ == '__main__':
    main()
