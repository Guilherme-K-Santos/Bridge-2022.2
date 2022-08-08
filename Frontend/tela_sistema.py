import PySimpleGUI as Interface


def excecao_apenas_numeros(numero_suposto):
    try:
        comparacao = int(numero_suposto)
        return comparacao
    except ValueError:
        return None


class TelaSistema:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def popup(self, mensagem: ''):
        Interface.Popup(mensagem)

    def tela_calculo(self):
        Interface.change_look_and_feel('DarkBrown4')
        layout = [
            [Interface.Text('Olá avaliadores!')],
            [Interface.Text('Por favor, adicionem o valor para o cálculo:')],
            [Interface.Text('Número Selecionado'), Interface.InputText('', key='numero')],
            [Interface.Button('Confirmar')]
        ]

        self.__window = Interface.Window('Desafio').Layout(layout)

    def tela_correcao(self):
        Interface.change_look_and_feel('DarkBrown3')
        layout = [
            [Interface.Text('Por favor, digite um número inteiro'), Interface.InputText('', key='numero_correcao')],
            [Interface.Button('Ok')]
        ]

        self.__window = Interface.Window('Correção').Layout(layout)

    def abrir_tela_calculo(self):
        self.tela_calculo()

        botao, valor = self.__window.Read()

        if botao:
            numero = valor['numero']
            numero_certo = excecao_apenas_numeros(numero)

            while numero_certo is None:
                self.close()
                self.popup('Por favor, coloque um valor númerico!')

                self.tela_correcao()
                botao, valor = self.__window.Read()
                if botao:
                    numero_correcao = valor['numero_correcao']
                    numero_certo = excecao_apenas_numeros(numero_correcao)
                else:
                    break

            self.close()
            return numero_certo
        else:
            exit()

    def tela_inicial(self):
        Interface.change_look_and_feel('DarkBrown2')
        layout = [
            [Interface.Text('Bem-vindos!')],
            [Interface.Text('Por favor, Selecione o que deseja:')],
            [Interface.Radio('Calcular', "tela_inicial", key=1)],
            [Interface.Radio('Histórico de Cálculos', "tela_inicial", key=2)],
            [Interface.Button('Confirmar')]
        ]

        self.__window = Interface.Window('Tela Inicial').Layout(layout)

    def abrir_tela_inicial(self):
        self.tela_inicial()
        botao, alternativas = self.__window.Read()

        opcao = None
        if botao:
            if alternativas[1]:
                opcao = 1
            elif alternativas[2]:
                opcao = 2
            else:
                self.popup('Selecione uma opção válida!')
        else:
            exit()

        self.close()
        return opcao
