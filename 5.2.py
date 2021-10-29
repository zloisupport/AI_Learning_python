﻿import matplotlib.pylab as plt # библиотека формирования графиков
import numpy as np  # библиотека математических функций
# Значения смещения
x = np.arange(-8,8,0.1)
b1 = -2
b2 = 0
b3 = 2
# Подписи значений смещения для отображения в легенде на графике
l1 = 'Смещение b = -2'
l2 = 'Смещение b = 0'
l3 = 'Смещение b = 2'

# цикл построения графиков для 3 значений смещения
for b, l in [(b1,l1),(b2,l2),(b3,l3)]: # организация цикла для трех значений
                                       # смещeния
    f = (1/(1+np.exp((-x+b)*1))) # функция сигмоиды
    plt.plot(x,f,label = 1) # построение графика для i-го смещения (Ы)


plt.xlabel('x')  # ПОДПИСЬ ОСИ Х
plt.ylabel('Y= f(x)')  # подпись оси у
plt.legend(loc=4) # место легенды на графике (4 - правый нижний угол)
plt.show() # вывод графиков