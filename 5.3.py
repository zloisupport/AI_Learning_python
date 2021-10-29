import numpy as np
# функция активации f(x) = 1 / (1+e^(-x))
def sigmoid(x):
    return 1/(1+np.exp(-x))

# создание класса нейрон
class Neuron:
    def __init__(self,w,b):
        self.w = w
        self.b = b
    
    def y(self,x): #Cумматор
        s = np.dot(self.w ,x)+self.b # Суммируем входы
        return sigmoid(s) # обращения к фукции активации


    

Xi = np.array([2,3]) # Задание вход знач x1 = 2, x2=3
Wi = np.array([0,1]) # Веса входных сенсоров W1= 0, w2= 1
bias = 4 # Смещение 
n = Neuron(Wi,bias) # Cоздание экзем класса Нейрон
print('Y=',n.y(Xi)) # Обращение к нейрону