# Листинг 5.4
import streamlit as st
import numpy as np

# Описание класса Нейрон
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    # функция активации
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return self.sigmoid(total)

# Описание класса Нейронная сеть из трех слоев
class OurNeuralNetwork:
    def __init__(self):
        weights = np.array([0, 1])  # веса (одинаковы для всех нейронов)
        bias = 0                    # смещение (одинаково для всех нейронов)

        # формируем сеть из трех нейронов
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)  # Формируем выход Y1 из нейрона h1
        out_h2 = self.h2.feedforward(x)  # Формируем выход Y2 из нейрона h2
        # Формируем выход Y из нейрона о1
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        return out_o1

# Создаем объект СЕТЬ из класса "Наша нейронная сеть"
network = OurNeuralNetwork()
# Формируем входные параметры для сети Х1=2, Х2=3
x = np.array([2, 3])
# Передаем входы в сеть и получаем результат
st.write("Y=", network.feedforward(x))