# Листинг 4.7
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Описание класса Perceptron
class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    # Рассчитать чистый вход
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    # Вернуть метку класса после единичного скачка
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Загрузка из файла массива - 150 элементов (объект DataFrame)
df = pd.read_csv('pages/glava_4/IRIS.csv', header=None)

# Выборка из объекта DF массива 100 элементов (столбец 0 и столбец 2),
# загрузка его в массив X (матрица)
X = df.iloc[0:99, [0, 2]].values

# Выборка из объекта DF 100 элементов (столбец 4 название цветков),
# загрузка его в одномерный массив Y
y = df.iloc[0:99, 4].values

# Преобразование названий цветков (столбец 4) в одномерный массив (вектор) из -1 и 1
y = np.where(y == 'Iris-setosa', -1, 1)

# Формирование параметров значений для вывода на график
# Первые 50 элементов (Строки 0-50, столбцы 0,1)
plt.scatter(X[0:49, 0], X[0:49, 1], color='red', marker='o', label='щетинистый')
# Следующие 50 элементов (Строки 50-100, столбцы 0,1)
plt.scatter(X[50:99, 0], X[50:99, 1], color='blue', marker='x', label='разноцветный')

tab_1, tab_2, tab_3 = st.tabs(['Группировка объектов',
                               'Ошибки обучения', 'Разделение объектов'])

# Формирование названий осей и вывод графика на экран
with tab_1:
    plt.xlabel('длина чашелистика')
    plt.ylabel('длина лепестка')
    plt.legend(loc='upper left')
    st.pyplot(plt)

# Создаем объект персептрон
ppn = Perceptron(eta=0.1, n_iter=10)

# Тренировка (обучение) персептрона
ppn.fit(X, y)

# Вывод данных об ошибках в процессе обучения
with tab_2:
    plt.clf()  # Очистить график от предыдущих данных
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Эпохи')
    # число ошибочно классифицированных случаев во время обновлений
    plt.ylabel('Число случаев ошибочной классификации')
    st.pyplot(plt)

# Визуализация разделительной границы
def plot_decision_regions(X, y, classifier, resolution=0.02):
    # настроить генератор маркеров и палитру
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'green', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # вывести поверхность решения
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # показать образцы классов
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8,
                    c=cmap(idx), marker=markers[idx], label=cl)

with tab_3:
    # Нарисовать картинку
    plt.clf()  # Очистить график от предыдущих данных
    plot_decision_regions(X, y, classifier=ppn)
    plt.xlabel('Длина чашелистика [см]')
    plt.ylabel('Длина лепестка [см]')
    plt.legend(loc='upper left')
    st.pyplot(plt)

# Данные для тестирования результатов обучения
i1 = [5.5, 1.6]
i2 = [6.4, 4.5]
st.write('Данные для тестирования')
st.text('i1 =' + str(i1) + ', i2 = ' + str(i2))

R1 = ppn.predict(i1)
R2 = ppn.predict(i2)

st.write('Результаты распознавания')
if R1 == -1:
    st.text('Цветок с параметрами' + str(i1) + ' - Iris setosa')
else:
    st.text('Цветок с параметрами' + str(i1) + ' - Iris versicolor')

if R2 == -1:
    st.text('Цветок с параметрами' + str(i2) + ' - Iris setosa')
else:
    st.text('Цветок с параметрами' + str(i2) + ' - Iris versicolor')