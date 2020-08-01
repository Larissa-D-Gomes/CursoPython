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

    def read(self, gamertag, password):
        if gamertag == '':
            raise MyException(INVALID_GAMERTAG)
        if gamertag not in self.dados:
            raise MyException(PLAYER_NOT_FOUND)

        player = self.dados[gamertag]
        if password != player.password:
            raise MyException(WRONG_PASSWORD)
        return player

    def update_gamertag(self, gamertag, new_gamertag, password):
        try:
            player = self.read(gamertag, password)

            if not self.player_exists(new_gamertag):
                del self.dados[gamertag]
                player.gamertag = new_gamertag

                self.dados[new_gamertag] = player
                self.salvar_dados()
                print('Gamertag alterada.')
                retorno = True
            else:
                print('Gamertag ja cadastrada.')
                retorno = False
        except MyException as e:
            raise e

        return retorno

    def delete(self, gamertag, password):
        try:
            self.read(gamertag, password)
            del self.dados[gamertag]
            self.salvar_dados()
            print('Player deletado com sucesso.')

        except MyException as e:
            raise e
        return  True

    def update_password(self, gamertag, password, new_password):
        try:
            self.read(gamertag, password)

            self.dados[gamertag].password = new_password
            self.salvar_dados()
            print('Senha alterada.')
            retorno = True

        except MyException as e:
            raise e

        return retorno

    def print_dados(self):
        for i in self.dados.items():
            print('=-'*20,'\n')
            print(i[1])

    def player_exists(self, gamertag):
        return False if not self.dados or self.dados.get(gamertag) is None else True


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
