# Листинг 4.8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Адаптивный линейный нейрон
class AdaptiveLinearNeuron(object):
    def __init__(self, rate=0.01, niter=10):
        self.rate = rate    # темп обучения
        self.niter = niter  # количество циклов обучения

    # Обучение
    def fit(self, X, y):
        self.weight = np.zeros(1 + X.shape[1])
        self.cost = []
        for i in range(self.niter):
            output = self.net_input(X)
            errors = y - output
            self.weight[1:] += self.rate * X.T.dot(errors)
            self.weight[0] += self.rate * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost.append(cost)
        return self

    # Вычисление чистого входного сигнала
    def net_input(self, X):
        return np.dot(X, self.weight[1:]) + self.weight[0]

    # Вычисление линейной активации
    def activation(self, X):
        return self.net_input(X)

    # Вычисление предсказания
    def predict(self, X):
        return np.where(self.activation(X) >= 0.0, 1, -1)

# Визуализация границы решений
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

# Загрузка из файла массива - 150 элементов (объект DataFrame)
df = pd.read_csv('IRIS.csv', header=None)

# выборка из объекта DF 100 элементов (столбец 4 название цветков),
# загрузка его в одномерный массив Y и печать
y = df.iloc[0:99, 4].values

# Преобразование названий цветков (столбец 4) в одномерный вектор из -1 и 1
y = np.where(y == 'Iris-setosa', -1, 1)

# выборка из объекта DF массива 100 элементов (столбец 0 и столбец 2),
# загрузка его в массив X (матрица) и печать
X = df.iloc[0:99, [0, 2]].values

# Создание макета для графика
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

# Обучение при rate = 0.01
aln1 = AdaptiveLinearNeuron(0.01, 10).fit(X, y)

# Передача результатов обучения в макет графика
ax[0].plot(range(1, len(aln1.cost) + 1), np.log10(aln1.cost), marker='o')
ax[0].set_xlabel('Эпохи')
ax[0].set_ylabel('log(Сумма квадратичных ошибок)')
ax[0].set_title('ADALINE Темп обучения  0.01')

# Обучение при rate = 0.0001
aln2 = AdaptiveLinearNeuron(0.0001, 10).fit(X, y)

# Передача результатов обучения в макет графика
ax[1].plot(range(1, len(aln2.cost) + 1), aln2.cost, marker='o')
ax[1].set_xlabel('Эпохи')
ax[1].set_ylabel('Сумма квадратичных ошибок')
ax[1].set_title('ADALINE Темп обучения 0.0001')
plt.show()

# Стандартизуем обучающую выборку
X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

# Обучение на стандартизованной выборке при rate = 0.01
aln = AdaptiveLinearNeuron(0.01, 10)
aln.fit(X_std,y)

# Строим график зависимости стоимости ошибок от эпох обучения
plt.plot(range(1, len(aln.cost) + 1), aln.cost, marker='o')
plt.xlabel('Эпохи')
plt.ylabel('Сумма квадратичных ошибок')
plt.show()

# Строим график с разделением области принятия решений
plot_decision_regions(X_std, y, classifier=aln)
plt.title('ADALINE (градиентный спуск)')
plt.xlabel('Длина чашелистика [стандартизованная]')
plt.ylabel('Длина лепестка [стандартизованная]')
plt.legend(loc='upper left')
plt.show()

# Данные для тестирования результатов обучения
i1 = [-1, -1]
i2 = [1, 1]
print('Данные для тестирования')
print('i1 = ', i1, 'i2 = ', i2)

# Обращение к обученному персептрону
R1 = aln.predict(i1)
R2 = aln.predict(i2)

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