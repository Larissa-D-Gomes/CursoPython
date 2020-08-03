"""Classe para armas"""

from ammunation import Ammunation
import time

class Weapon:
    def __init__(self, name, accuracy, damage, reload_speed, ammunition, muzzle, barrel, laser, optic):

        self.name = name
        self.accuracy = accuracy
        self.damage = damage
        self.reload_speed = reload_speed
        self.ammunition = ammunition

        self.muzzle = muzzle
        self.barrel = barrel
        self.laser = laser
        self.optic = optic

    def shoot(self):
        pass

    def reload(self):
        pass