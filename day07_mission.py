#10.7



el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return(f'{self.name},안녕 {self.symbol}, {self.number}')


hydrogen = Element(**el_dict)
print(hydrogen)



