import math
class CSVFile():

    def __init__(self, name):
        # meglio fare isinstance 
        if not isinstance(name, str):
        # if type(name) is not str:
            raise Exception('Name file non è stringa')
        self.name = name

    def get_data(self, start = None, end = None):
        try:
            start = int(float(start))
            end = int(float(end))
        except (ValueError, TypeError):
            print('Errore nei start ed end')
            return []
        try: 
            math.sqrt(end-start)
        except ValueError:
            print('Errore: start > end')
            return []
        lista = []
        try:
            file = open(self.name, 'r')       
        except OSError:
            print('Errore: apertura file')
            return [] 
        else:
            i = 0
            for line in file:
                i += 1
                if i >= start and i <= end:
                    elements = line.split(',')
                    # if elements[0].startswith('Date'):
                    #     pass
                    # else:
                    elements[-1] = elements[-1].strip()
                    lista.append(elements)
            return lista

class NumericalCSVFile(CSVFile):

    def get_data(self, *args, **kwargs):
        
        string_data = super().get_data(*args, **kwargs)
        
        lista = []
        for string_row in string_data:
            try:
                string_row[-1] = float(string_row[-1])
                lista.append(string_row)
            except Exception as e:
                print('Errore di valore: "{}"'.format(e))
                pass
        return lista
            

# file = NumericalCSVFile('shampoo_sales.txt')
# print(file.get_data())

# file = CSVFile('shampoo_sales.txt')
# print(file.get_data(start = 1, end = 5))
# file = NumericalCSVFile('shampoo_sales.txt')
# print(file.get_data(start = '', end = 5))