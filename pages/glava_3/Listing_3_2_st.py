# Листинг 3.2
import numpy as np

# Создание класса "Нейрон"
class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):            # Сумматор
        s = np.dot(self.w, x)  # Суммируем входы
        return s               # функция активации

Xi = np.array([1, 0, 0, 1])    # Задание значений входам
Wi = np.array([5, 4, 3, 1])    # Веса входных сенсоров
n = Neuron(Wi)                 # Создание объекта из класса Neuron
st.write('S= ', n.y(Xi))       # Обращение к нейрону