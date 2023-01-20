#10.4

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

ele = Element('Hydrogen', 'H', 1)
print(ele.symbol)
