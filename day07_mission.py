#10.5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

class Element:
    def __init__(self, eldict):
        self.name = eldict['name']
        self.symbol = eldict['symbol']
        self.number = eldict['number']

hydrogen = Element(el_dict)
print(hydrogen.name)

