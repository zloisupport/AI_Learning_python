﻿# ROST VES 
import numpy as np

def sigmoid(x):
    # Функция активации sigmoid -f(X)=1/(1+e^(-x))
    return 1/(1+np.exp(-x))

def deriv_sigmoid(x):
    # Производная от Sigmoid - f'(x) = f(x)*(1-f(x))
    fx = sigmoid(x)
    return fx * (1-fx)

# Расчет среднеквадратической ошибки
def mse_loss(y_true,y_pred):
    # y_true , y_pred является массивами numpy c одинаковой длиной
    return ((y_true - y_pred)**2).mean()

class OurNeutralNetwork:
    def __init__(self):
        # Вес
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        # Смещение
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()
    
    def feedforkward(self,x):
        # x Являестя массивом numpy c двумя элементами
        h1 = sigmoid(self.w1*x[0]+self.w2*x[1]+self.b1)
        h2 = sigmoid(self.w3*x[0]+self.w4*x[1]+self.b2)
        o1 = sigmoid(self.w5*h1+self.w6*h2+self.b2)
        return o1

    def train(self,data,all_y_trues):
        learn_rate = 0.1
        epochs  = 10000 #Кол-во циклов во всем набре данных

        for epoch in range(epochs):
            for x,y_true in zip(data,all_y_trues):
                # -- выполняем обратную связь (нам понадобиться эти значения в дальнейшем)
                sum_h1 = self.w1 * x[0]+self.w2*x[1]+self.b1
                h1 = sigmoid(sum_h1) 

                sum_h2 = self.w3 * x[0]+self.w4*x[1]+self.b1
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 *h1 +self.w6*h2+self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1
                # -- Подсчет частных производных
                # -- Наименование d_L_d_w1 пред-т частично L / w1
                d_L_d_ypred = -2*(y_true - y_pred)

                # Нейрон о1
                d_ypred_d_w5  = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6  = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3  = deriv_sigmoid(sum_o1)

                d_ypred_d_h1  = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2  = self.w6 * deriv_sigmoid(sum_o1)

                #Нейрон h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)
                
                #Нейрон h2
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)

                # -- обновляем вес и смешение 
                # Нейрон h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                # Нейрон h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h1_d_b1

                # Нейрон o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

                # --Подсчитываем общую потерю в конце каждой фазы
                if epoch % 100 == 0:
                    y_preds = np.apply_along_axis(self.feedforkward,1,data)
                    loss = mse_loss(all_y_trues,y_preds)
                    print("Epoch %d loss: %.3f"%(epoch,loss))
        # Опр набор данных
        data = np.array([
            [-2,-1],  #Alice
            [25,6],  #Bob
            [17,4],  #Charlie
            [-15,-6],  #Diana
        ])
        
        all_y_trues = np.array([
            1,#Alice
            0,#Bob
            0,#Charlie
            1,#Diana
        ]) 

        network = OurNeutralNetwork()
        network.train(data,all_y_trues) 





