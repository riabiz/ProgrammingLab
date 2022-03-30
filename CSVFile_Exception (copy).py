class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        lista = []
        try:
            file = open(self.name, 'r')   
            
        except OSError:
            print('Errore: apertura file')
            return [] 
        else:
            for line in file:
                elements = line.split(',')
                if elements[0].startswith('Date'):
                    pass
                else:
                    elements[-1] = elements[-1].strip()
                    lista.append(elements)
            return lista
            

# file = CSVFile('shampoo_sals.txt')
# print(file.get_data())