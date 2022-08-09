from Backend.DAO import BancoDados


class DAONumeros(BancoDados):
    def __init__(self):
        super().__init__("Numeros.pkl")

    def add(self, numero, resultado):
        super().add(numero, resultado)

    def get(self, numero):
        return super().get(numero)

    def get_all(self):
        return super().get_all()
