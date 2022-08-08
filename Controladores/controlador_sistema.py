from Frontend.tela_sistema import TelaSistema
from Backend.DAO import BancoDados


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__banco_de_dados = BancoDados()

    def iniciar(self):
        numero = self.__tela_sistema.abrir_tela_inicial()
