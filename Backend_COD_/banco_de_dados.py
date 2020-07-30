"""Classe para salvar dados de novos jogadores cadastrados"""

import os
import pickle
from my_exception import *
from player import Player

class Database:
    def __init__(self):
        self.dados = {}
        self.carregar_dados()#carregar dados do HDD para RAM

    """Funcao para criar player no banco de dados"""
    def create(self, gamertag, password):
        if gamertag == '':
            raise MyException(INVALID_GAMERTAG)
        if gamertag in self.dados:
            raise MyException(PLAYER_ALREADY_REGISTERED)
        self.dados[gamertag] = Player(gamertag, password)
        print(self.salvar_dados())


    def print_dados(self):
        for i in self.dados.items():
            print('=-'*20,'\n')
            print(i[1])


    """Funcao para carregar dados de arquivo para o programa,
       caso o arquivo nao exista ele sera criado"""
    def carregar_dados(self):

        # Verificar existencia de arquivo
        if not os.path.isfile(os.path.join(os.getcwd(), 'players.pkl')):

            try:#Se arquivo nao existir, criar com escrita binaria
                with open(os.path.join(os.getcwd(), 'players.pkl'), 'wb') as file:
                    pickle.dump({}, file, pickle.HIGHEST_PROTOCOL)
                    retorno = True
                print('Arquivo aberto com sucesso!')

            except FileNotFoundError as e1:
                raise e1
                retorno = False
            except Exception as e2:
                raise e2
                retorno = False
        else:
            try:
                # Abrindo o arquivo em modo de leitura binaria
                with open('players.pkl', 'rb') as file:
                    self.dados = pickle.load(file)
                    print('Dados carregados com sucesso!')
                    retorno = True
            except FileNotFoundError:
                print('ERRO: ARQUIVO NAO ENCONTRADO')

        return retorno

    def salvar_dados(self):

        try:
            # Abrindo o arquivo em modo de escrita binaria
            with open('players.pkl', 'wb') as file:
                pickle.dump(self.dados, file, pickle.HIGHEST_PROTOCOL)

            print('Dados salvos com sucesso!')
            retorno = True

        except FileNotFoundError:
            print('ERRO: ARQUIVO NAO ENCONTRADO')
            retorno = False
        return retorno
