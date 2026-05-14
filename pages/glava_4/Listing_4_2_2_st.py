# Листинг 4.2.2
import numpy as np
import streamlit as st

# Класс перцептрон
class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    # Обучение
    def fit(self, X, y):
        # Инициализация весов и смещения случайными значениями
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = 1 if linear_output >= 0 else 0

                # Обновление весов и смещения при ошибке классификации
                if y[idx] != y_predicted:
                    self.weights += self.learning_rate * (y[idx] - y_predicted) * x_i
                    self.bias += self.learning_rate * (y[idx] - y_predicted)

    # Предсказание
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.where(linear_output >= 0, 1, 0)

# Функция предсказания результатов
def my_car(car):
    if car == 0:
        st.write('Автомобиль может ехать ----------->')
    else:
        st.write('Автомобиль должен стоять <-----------')

# Исходные данные для операции OR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Правильные ответы для операции OR
y = np.array([0, 1, 1, 1])

# Создание модели
model = Perceptron()
# Обучение модели
model.fit(X, y)

# Проверка работы перцептрона
st.write('Свет зеленый, нет пешеходов x=[0, 0]')
x = [0, 0]
my_car(model.predict(x))

st.write('Свет красный, нет пешеходов x=[1, 0]')
x = [1, 0]
my_car(model.predict(x))

st.write('Свет зеленый, есть пешеходы x=[0, 1]')
x = [0, 1]
my_car(model.predict(x))

st.write('Свет красный, есть пешеходы x=[1, 1]')
x = [1, 1]
my_car(model.predict(x))
