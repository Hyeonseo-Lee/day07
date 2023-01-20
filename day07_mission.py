#10.6

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(f'{self.name}, {self.symbol}, {self.number}')

hydrogen = Element(**el_dict)
hydrogen.dump()
