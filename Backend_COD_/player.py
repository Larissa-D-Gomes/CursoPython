"""Classe para salvar dados de jogador"""

class Player:
    def __init__(self, gamertag, password):
        self.gamertag = gamertag
        self.password = password
        self.total_wins = 0
        self.favorite_loadout = None
        self.loudout = []

    def __str__(self):
        return (f'Gamertag: {self.gamertag}\n'
                f'Senha: {self.password}\n'
                f'Total da vitorias: {self.total_wins}\n'
                f'Loadout favorito: {self.favorite_loadout}\n'
                f'Loudouts: {self.loudout}\n')