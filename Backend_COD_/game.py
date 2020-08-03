"""Classe Game"""

from banco_de_dados import *

class Game:
    def __init__(self):
        self.online_players = []
        self.db = Database()
        self.menu()

    def print_acoes(self):
        input('\nInsira qualquer tecla para continuar... ')
        print(f'{"=" * 10} MENU PRINCIPAL {"=" * 10}')
        print('[ 1 ] - LOGIN\n'
              '[ 2 ] - CRIAR CONTA\n'
              '[ 3 ] - ALTERAR GAMERTAG\n'
              '[ 4 ] - ALTERAR SENHA\n'
              '[ 5 ] - DELETAR CONTA\n'
              '[ 6 ] - FECHAR JOGO')

    def menu(self):
        acao = 0
        while acao != '6':
            self.print_acoes()
            acao = input('\nINSIRA A ACAO: ')

            if acao == '1':
                self.login()
            elif acao == '2':
                self.create_player_account()
            elif acao == '3':
                self.update_player_gamertag()
            elif acao == '4':
                self.update_player_password()
            elif acao == '5':
                self.delete_player_account()
            elif acao == '6':
                print('Saindo do jogo...')
            else:
                print('OPCAO INVALIDA.')

            #self.db.print_dados()
            for i in online_players:
                print(i)

    def create_player_account(self):
        aux = False
        print(f'{"=" * 10} CRIAR CONTA {"=" * 10}')

        while aux != True:
            try:
                gamertag = input('\nDigite a Gamertag: ')
                senha = input('Digite a senha: ')
                aux = self.db.create(gamertag, senha)
            except MyException as e:
                print(e)

    def delete_player_account(self):
        aux = False
        print(f'{"=" * 10} DELETAR CONTA {"=" * 10}')

        while aux != True:
            try:
                gamertag = input('\nDigite a Gamertag: ')
                senha = input('Digite a senha: ')
                aux = self.db.delete(gamertag, senha)
            except MyException as e:
                print(e)

    def update_player_gamertag(self):
        aux = False
        print(f'{"=" * 10} ALTERAR GAMERTAG {"=" * 10}')

        while aux != True:
            try:
                gamertag = input('\nDigite a Gamertag: ')
                senha = input('Digite a senha: ')
                new_gamertag = input('\nDigite a nova Gamertag: ')
                aux = self.db.update_gamertag(gamertag, new_gamertag, senha)
            except MyException as e:
                print(e)

    def update_player_password(self):
        aux = False
        print(f'{"=" * 10} ALTERAR GAMERTAG {"=" * 10}')

        while aux != True:
            try:
                gamertag = input('\nDigite a Gamertag: ')
                password = input('Digite a senha: ')
                new_password = input('\nDigite a nova senha: ')
                aux = self.db.update_password(gamertag, password, new_password)
            except MyException as e:
                print(e)

    def login(self):
        try:
            gamertag = input('\nDigite a Gamertag: ')
            password = input('Digite a senha: ')
            p = self.db.read(gamertag, password)
            self.online_players.append(p)
        except MyException as e:
            print(e)


