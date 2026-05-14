# Листинг 3.5
import numpy as np

# Создание класса "Нейрон"
class Neuron:
    def __init__(self, w):
        self.w = w

    # функция активации: f(x) = 1 / (1 + e^(-x))
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def y(self, x):             # Сумматор
        s = np.dot(self.w, x)   # Суммируем входы
        y = self.sigmoid(s)     # Обращение к функции активации
        return y                # функция активации

Xi = np.array([0, 0, 1, 1])   # Задание значений входам
Wi = np.array([5, 4, 3, 1])   # Веса входных сенсоров
n = Neuron(Wi)                # Создание объекта из класса Neuron
st.write('Y= ', n.y(Xi))         # Обращение к нейрону