# Листинг 3.1
# Модуль Neuron
import numpy as np
import streamlit as st

# Создание класса "Нейрон"
class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):            # Сумматор
        s = np.dot(self.w, x)  # Суммируем входы
        return s               # функция активации

Xi = np.array([2, 3])          # Задание значений входам
Wi = np.array([1, 1])          # Веса входных сенсоров
n = Neuron(Wi)                 # Создание объекта из класса Neuron
st.write('S1= ', n.y(Xi))      # Обращение к нейрону
Xi = np.array([5, 6])          # Веса входных сенсоров
st.write('S2= ', n.y(Xi))      # Обращение к нейрону