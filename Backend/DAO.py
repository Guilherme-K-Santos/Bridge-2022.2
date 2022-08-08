import pickle


class BancoDados:
    def __init__(self):
        self.__nome_arquivo = 'numeros.pkl'
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):
        self.__cache = pickle.load(open(self.__nome_arquivo, 'rb'))

    def __dump(self):
        pickle.dump(self.__cache, open(self.__nome_arquivo, 'wb'))

    def add(self, key, numero):
        self.__cache[key] = numero
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None
