# Листинг 6.6
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st

# Загрузка набора данных
iris_dataset = load_iris()
# Формирование обучающих и тестовых данных
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                   iris_dataset['target'], random_state=0)
# Создание сети
knn = KNeighborsClassifier(n_neighbors=1)
# Обучение сети
knn.fit(X_train, y_train)

# Создание контрольных данных для цветка ирис
X_new = np.array([[5, 2.9, 1, 0.2]])
# Прогноз на контрольных данных
pr = knn.predict(X_new)
st.write("Метка вида цветка: {}".format(pr))
st.write("Вид цветка: {}".format(iris_dataset['target_names'][pr]))