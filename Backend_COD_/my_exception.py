"""Classe para tratamento de excessoes"""

INVALID_GAMERTAG = 'Gamertag invalida.'
PLAYER_ALREADY_REGISTERED = 'Esta gamertag ja foi utilizada. Tente outra.'
PLAYER_NOT_FOUND = 'Gamertag nao encontrada.'
WRONG_PASSWORD = 'Senha incorreta.'

class MyException(Exception):
    pass