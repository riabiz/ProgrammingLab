som = sum([1,2])
print('la somma è pari a: {}'.format(som))

def somma(lista):
    sum = 0
    for element in lista:
        sum += element
    return sum

som = somma([1,2])
print('la somma è pari a: {}'.format(som))