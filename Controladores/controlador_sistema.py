import math
import time

from Backend.DAO_numeros import DAONumeros
from Frontend.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__daonumeros = DAONumeros()

    def iniciar(self):
        opcao = self.__tela_sistema.abrir_tela_inicial()
        if opcao == 1:
            self.calculo()
        elif opcao == 2:
            self.historico()
        else:
            self.iniciar()

    def calculo(self):
        numero = self.__tela_sistema.abrir_tela_calculo()

        if numero is None:
            self.iniciar()

        comeco_tempo = time.time()

        dividendo = numero
        resultado_final = 0
        num_divisores_n1 = -math.inf

        while dividendo > 1:

            divisor = 2
            if dividendo % 2 == 0:
                num_divisores_n = 2
                while divisor <= dividendo/2:
                    if dividendo % divisor == 0:
                        num_divisores_n += 1
                    divisor += 1
                dividendo -= 1
            elif dividendo % 3 == 0:
                num_divisores_n = 2
                while divisor <= dividendo/3:
                    if dividendo % divisor == 0:
                        num_divisores_n += 1
                    divisor += 1
                dividendo -= 1
            elif dividendo % 5 == 0:
                num_divisores_n = 2
                while divisor <= dividendo/5:
                    if dividendo % divisor == 0:
                        num_divisores_n += 1
                    divisor += 1
                dividendo -= 1
            elif dividendo % 7 == 0:
                num_divisores_n = 2
                while divisor <= dividendo/7:
                    if dividendo % divisor == 0:
                        num_divisores_n += 1
                    divisor += 1
                dividendo -= 1
            else:
                num_divisores_n = 2
                dividendo -= 1

            if num_divisores_n1 == num_divisores_n:
                resultado_final += 1

            num_divisores_n1 = num_divisores_n

        fim_tempo = time.time()

        self.__daonumeros.add(numero, resultado_final)
        self.__tela_sistema.abrir_resultado_final(numero, resultado_final, (fim_tempo - comeco_tempo))

        self.iniciar()

    def historico(self):
        guarda = []
        numero, resultado = self.__daonumeros.get_all()

        contador = 0
        for num in numero:
            guarda.append({num: resultado[contador]})
            contador += 1

        resposta_tela = self.__tela_sistema.abrir_historico(guarda)

        if resposta_tela is None or True:
            self.iniciar()
