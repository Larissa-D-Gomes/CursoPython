"""Classe para tratamento de excessoes"""

INVALID_GAMERTAG = 'Gamertag invalida.'
PLAYER_ALREADY_REGISTERED = 'Esta gamertag ja foi utilizada. Tente outra.'
class MyException(Exception):
    pass