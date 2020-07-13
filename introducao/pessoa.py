
class Pessoa:
    """Construtor de pessoa, recebe String para
        atributos nome, idade e sexo.
    """
    def __init__(self, nome, idade, sexo):

        try:
            if nome == '' or (sexo != 'F' and sexo != 'M'):
                raise ValueError

            self.nome = nome
            self.idade = int(idade)
            self.sexo = sexo
        except ValueError:
            raise ValueError

    def setNome(self, nome):
        if nome == "":
            raise ValueError
        self.nome = nome

    def setIdade(self, idade):
        try:
            self.idade = int(idade)
        except ValueError:
            raise ValueError

    def setSexo(self, sexo):
        if sexo != 'F' and sexo != 'M':
            raise ValueError

        self.sexo = sexo

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getSexo(self):
        return self.sexo

    def __str__(self):
        return f'Nome: {self.nome} \nIdade: {self.idade} \nSexo: {self.sexo}'
