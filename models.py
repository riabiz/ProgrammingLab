class Model():

    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')    


class IncrementModel(Model):

    def predict(self, data):
        n = 2
        if len(data) < n:
            raise Exception('Errore: lista troppo corta')
        elif not isinstance(data, list):
            raise Exception('Errore: non hai una lista')
        data = data[-(n+1):]
        increments = []
        for index, item in enumerate(data):
            next = index + 1
            print(next, len(data))
            if next < len(data):
                incr = data[next] - item
            else:
                return sum(increments)/n + item
            increments.append(incr)

# lista = [ 50, 52, 60]
# incrementmodel = IncrementModel()
# predict = incrementmodel.predict(lista)
# print(predict)
