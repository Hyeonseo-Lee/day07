#10.8


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
        @property
        def names(self):
            return (self.__name, self.__symbol, self.__number)
        @name.setter
        def name2(self, name):
            self.__name = name
            # self.__symbol = symbol
            # self.__number = number

    # def __str__(self):
    #     return(f'{self.name},안녕 {self.symbol}, {self.number}')


hydrogen = Element("Hydden","H",1)
hydrogen.names()
print(hydrogen)




