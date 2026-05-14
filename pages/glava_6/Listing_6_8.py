# Листинг 6.8
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Загрузка исходных данных
iris = datasets.load_iris()
# Выбор размеров лепестков
X = iris.data[:, [2, 3]]
y = iris.target

# # Формирование обучающих и тестовых данных
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=0)
# Стандартизация признаков
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Создание перцептрона
ppn = Perceptron(eta0=0.1, random_state=0, max_iter=40)
# Обучение перцептрона
ppn.fit(X_train_std, y_train)
# Прогноз на обученном перцептроне
y_pred = ppn.predict(X_test_std)
print('Число ошибочно классифицированных образцов: % d' % (y_test != y_pred).sum())
print('Верность: %.2f' % accuracy_score(y_test, y_pred))

def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # настроить генератор маркеров и палитру
    markers = ('s', 'x', 'o', '>', 'v')
    colors = ('red', 'blue', 'green', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # вывести поверхность решения
    xl_min, xl_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xxl, xx2 = np.meshgrid(np.arange(xl_min, xl_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xxl.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xxl.shape)
    plt.contourf(xxl, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xxl.min(), xxl.max())
    plt.ylim(xx2.min(), xx2.max())
    # показать все образцы
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)
        # выделить тестовые образцы
        if test_idx:
            X_test, y_test = X[test_idx, :], y[test_idx]
            plt.scatter(X_test[:, 0], X_test[:, 1], c='0', alpha=1.0,
                        linewidths=1, marker='.', s=55, label='тест набор')

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
plot_decision_regions(X=X_combined_std, y=y_combined, classifier=ppn,
                      test_idx=range(105, 150))
plt.xlabel('Длина лепестка [стандартизованная]')
plt.ylabel('Ширина лепестка [стандартизованная]')
plt.legend(loc='upper left')
plt.show()