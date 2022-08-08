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

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()
