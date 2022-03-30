from Lezione6 import CSVFile

def test_CSVFile(CSVFile, name_file):
    file = CSVFile(name_file)
    if hasattr(file, 'name'):
        print('OK!')
    else:
        print('ERRORE!')

test_CSVFile( CSVFile, 'prova.txt')