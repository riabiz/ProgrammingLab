class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista = []
        file = open(self.name, 'r')
        for line in file:
            elements = line.split(',')
            if elements[0].startswith('Date'):
                pass
            else:
                elements[-1] = elements[-1].strip()
                lista.append(elements)
        return lista



file = CSVFile('shampoo_sales.txt')
print(file.get_data())