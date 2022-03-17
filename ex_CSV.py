def sum_csv(file_name):
    if not file_name:
        return None
    else:
        values = []
        file = open(file_name, 'r')
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                values.append(float(elements[1]))
        file.close()
        tot = 0
        for v in values:
            tot += v
        return tot

# print(sum_csv('shampoo_sales.txt'))