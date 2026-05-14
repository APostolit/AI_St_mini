# Листинг 6.7
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Загрузка набора данных
iris_dataset = load_iris()
# Формирование обучающих и тестовых данных
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'],
                                   iris_dataset['target'], random_state=0)
# Создание сети
knn = KNeighborsClassifier(n_neighbors=1)
# Обучение сети
knn.fit(X_train, y_train)
# Прогноз на тестовых данных
pr = knn.predict(X_test)
print("Прогноз вида на тестовом наборе:\n {}".format(pr))
print("Точность прогноза на тестовом наборе:{:.2f}".format(np.mean(pr == y_test)))
