# Листинг 5.3
import numpy as np

# Создание класса Нейрон
class Neuron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    # функция активации: f(x) = 1 / (1 + e^(-x))
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def y(self, x):                     # Сумматор
        s = np.dot(self.w, x) + self.b  # Суммируем входы
        return self.sigmoid(s)          # обращение к функции активации

Xi = np.array([2, 3])  # Задание значений входам x1 = 2, x2 = 3
Wi = np.array([0, 1])  # Веса входных сенсоров w1 = 0, w2 = 1
bias = 4               # Смещение b = 4
n = Neuron(Wi, bias)   # Создание объекта из класса Neuron
print('Y=', n.y(Xi))   # Обращение к нейрону

for bias in range(-4, 5):
    n = Neuron(Wi, bias)
    print('bias=', bias, ' Y=', n.y(Xi))
