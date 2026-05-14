# Листинг 3.3
import numpy as np

# Создание класса "Нейрон"
class Neuron:
    def __init__(self, w):
        self.w = w

    # Функция активации
    def onestep(self, x):
        b = 5
        if x >= b:
            return 1
        else:
            return 0

    # Сумматор
    def y(self, x):             # Сумматор
        s = np.dot(self.w, x)   # Суммируем входы
        y = self.onestep(s)     # Обращение к функции активации
        return y

Xi = np.array([1, 0, 0, 1])   # Задание значений входам
Wi = np.array([5, 4, 3, 1])   # Веса входных сенсоров
n = Neuron(Wi)                # Создание объекта из класса Neuron
print('Y= ',n.y(Xi))          # Обращение к нейрону