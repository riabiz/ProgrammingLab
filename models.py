class Model():

    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def evaluate(self, data):
        # Evaluate non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
        

class IncrementModel(Model):

    def avg_increment(self, data):
        prev_item = None

        increments = []

        for item in data:
            if prev_item is not None:
                increments.append(item - prev_item)
                
            prev_item = item
        try:
            avg = sum(increments)/(len(data)-1)
        except ZeroDivisionError:
            print('Errore: la lista è vuota')
        return avg

    def predict(self, data):

        avg_increment = self.avg_increment(data)

        return avg_increment + data[-1]

    def evaluate(self, evaluation_dataset):
        sum_error = 0
        for index, item in enumerate(evaluation_dataset):
            if index == len(evaluation_dataset) - 3:
                return sum_error/index
            prediction = self.predict(evaluation_dataset[index: index + 3])
            sum_error +=  abs( evaluation_dataset[index + 3] - prediction )
            
            


class FitIncrementModel(IncrementModel):

    def fit(self, fit_data):
        self.global_avg_increment = self.avg_increment(fit_data)

    def predict(self, predict_data):
        # Chiamo la predict della classe genitore "IncrementModel"
        parent_prediction = super().predict(predict_data)

        # Sottraggo l'ultimo valore alla predizione del genitore
        # cosi' da avre l'incremento "originale"
        parent_predict_increment = parent_prediction - predict_data[-1]

        # Ora medio l'incremento del fit con quello della predict
        prediction_increment = (self.global_avg_increment + parent_predict_increment) / 2

        # E lo ri-sommo all'ultimo elemento
        prediction = predict_data[-1] + prediction_increment

        return prediction

'''
lista = [ 50, 52, 60]
incrementmodel = IncrementModel()
predict = incrementmodel.predict(lista)
print(predict)

fit_data = [8,19,31,41]
predict_data = [50,52,60]
fit_increment_model = FitIncrementModel()
fit_increment_model.fit(fit_data)
prediction = fit_increment_model.predict(predict_data)
print(prediction)'''
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

n = 25
fit_data = shampoo_sales[0:n]
evaluate_data = shampoo_sales[n:-1]
eval_increment_model = IncrementModel()
eval = eval_increment_model.evaluate(evaluate_data)
print(eval)
print('')
'''
eval_increment_model = FitIncrementModel()
eval = eval_increment_model.evaluate(evaluate_data)
print(eval)'''