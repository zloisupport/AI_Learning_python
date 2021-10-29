import numpy as np

# Функция активации
def sigmoid(x):
    return 1 / (1+np.exp(-x))


# Создание класса Нейрон
class Neuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias

    def feedforwards(self,inputs):
        total = np.dot(self.weights,inputs)+self.bias
        return sigmoid(total)

# Описание класса Нейроная сеть из 3 слоев
class OurNeutralNetwork:

    def __init__(self):
        weights = np.array([0,1]) #веса  (одинаковых нейронов)
        bias = 0 # Смещение (одинаковых для всех нейронов)
        
        # формируем сеть из трех нейронов
        self.h1= Neuron(weights,bias)
        self.h2= Neuron(weights,bias)
        self.o1= Neuron(weights,bias)
    
    def feedforwards(self,x):
        out_h1= self.h1.feedforwards(x) # Формируем выход Y1 из Нейрона h1
        out_h2= self.h2.feedforwards(x) # Формируем выход Y2 из Нейрона h2
        out_o1= self.o1.feedforwards(np.array([out_h1,out_h2])) # Формируем выход Y из Нейрона o1

        return out_o1

network = OurNeutralNetwork() # Создаем обьект сеть из класса" Наша нейронная сеть"
x= np.array([2,3]) # Формируем входные параметры для сети X1= 2 X2=3
print("Y= ",network.feedforwards(x)) # Передаем входы в сеть и получаем результат