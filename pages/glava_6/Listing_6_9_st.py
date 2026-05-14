# Листинг 6.9
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
import streamlit as st

# Загрузка исходных данных
iris = datasets.load_iris()
# Выбор размеров лепестков
X = iris.data[:, [2, 3]]
y = iris.target
# # Формирование обучающих и тестовых данных
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
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
                        linewidths=1, marker='.', s=55,
            label='тест набор')

# Формирование графика
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

Lr = LogisticRegression(C=1000.0, random_state=0)
Lr.fit(X_train_std, y_train)
plot_decision_regions(X_combined_std, y_combined, classifier=Lr,
                      test_idx=range(105, 150))
plt.xlabel('Длина лепестка [стандартизированная]')
plt.ylabel('Ширина лепестка [стандартизированная]')
plt.legend(loc='upper left')
st.pyplot(plt)

# Прогноз для трех видов цветка
X1 = np.array([[1.5, 1.5]])
X2 = np.array([[0.0, 0.0]])
X3 = np.array([[-1, -1]])
p1 = Lr.predict_proba(X1)
p2 = Lr.predict_proba(X2)
p3 = Lr.predict_proba(X3)

with st.container(width=300):
    st.write('Вариант 1')
    st.text(X1)
    st.write(p1)

    st.write('Вариант 2')
    st.text(X2)
    st.write(p2)

    st.write('Вариант 3')
    st.text(X3)
    st.write(p3)