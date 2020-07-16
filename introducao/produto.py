class Produto:
    """Construtor de produto, recebe String para
       nome e float para preco.
    """
    def __init__(self, nome, preco):
        if (not type(preco) is float) or (not type(nome) is str) or preco <= 0.0:
            raise ValueError

        self.preco = preco
        self.nome = nome

    def getPreco(self):
        return self.preco

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        if not type(nome) is str:
            raise ValueError
        self.nome = nome

    def setPreco(self, preco):
        if not type(preco) is float or preco <= 0.0:
            raise ValueError
        self.preco = preco

