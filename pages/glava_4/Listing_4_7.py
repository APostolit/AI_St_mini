# Листинг 4.7
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

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
df = pd.read_csv('IRIS.csv', header=None)
# print('Массив')
# print(df.to_string())

# выборка из объекта DF массива 100 элементов (столбец 0 и столбец 2),
# загрузка его в массив X (матрица) и печать
X = df.iloc[0:99, [0, 2]].values
# print('Значение X - 100')
# print(X)
# print('Конец X')

# Выборка из объекта DF 100 элементов (столбец 4 название цветков),
# загрузка его в одномерный массив Y и печать
y = df.iloc[0:99, 4].values
# print('Значение четвертого столбца Y - 100')
# print(y)

# Преобразование названий цветков (столбец 4) в одномерный массив (вектор) из -1 и 1
y = np.where(y == 'Iris-setosa', -1, 1)
print('Значение названий цветков  в виде -1 и 1, Y - 100')
print(y)

# Формирование параметров значений для вывода на график
# Первые 50 элементов (Строки 0-50, столбцы 0,1)
plt.scatter(X[0:49, 0], X[0:49, 1], color='red', marker='o', label='щетинистый')
# Следующие 50 элементов (Строки 50-100, столбцы 0,1)
plt.scatter(X[50:99, 0], X[50:99, 1], color='blue', marker='x', label='разноцветный')

# Формирование названий осей и вывод графика на экран
plt.xlabel('длина чашелистика')
plt.ylabel('длина лепестка')
plt.legend(loc='upper left')
plt.show()

# Создаем объект персептрон
ppn = Perceptron(eta=0.1, n_iter=10)

# Тренировка (обучение) персептрона
ppn.fit(X, y)

# Вывод данных об ошибках в процессе обучения
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Эпохи')
# число ошибочно классифицированных случаев во время обновлений
plt.ylabel('Число случаев ошибочной классификации')
plt.show()
#print(X)

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

# Нарисовать график
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('Длина чашелистика [см]')
plt.ylabel('Длина лепестка [см]')
plt.legend(loc='upper left')
plt.show()

# Данные для тестирования результатов обучения
i1 = [5.5, 1.6]
i2 = [6.4, 4.5]
print('Данные для тестирования')
print('i1 = ', i1, 'i2 = ', i2)

# Обращение к обученному персептрону
R1 = ppn.predict(i1)
R2 = ppn.predict(i2)
print('Результаты распознавания')
print('R1=', R1, '  R2=', R2)

if R1 == -1:
    print('Цветок с параметрами', i1)
    print('R1= Вид - Iris setosa')
else:
    print('Цветок с параметрами', i1)
    print('R1= Вид - Iris versicolor')

if R2 == -1:
    print('Цветок с параметрами', i2)
    print('R2= Вид - Iris setosa')
else:
    print('Цветок с параметрами', i2)
    print('R2= Вид - Iris versicolor')
