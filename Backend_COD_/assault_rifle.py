from weapon import Weapon

#Classe que herda todoas atributos de Weapon
class AssaultRifle(Weapon):
    def __init__(self, name, accuracy, damage, reload_speed, ammunition, muzzle, barrel,
            laser,  optic, stock, underbarrel):
        #construtor de weapon
        super.__init__(name=name, accuracy=accuracy, damage=damage,
            reload_speed=reload_speed, ammunition=ammunition,
            muzzle=muzzle, barrel=barrel, laser=laser, optic=optic)

        #atributos especificos
        self.stock = stock
        self.underbarrel = underbarrel

    def shoot(self):
        pass

    def reload(self):
        pass


