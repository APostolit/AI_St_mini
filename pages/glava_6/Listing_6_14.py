# Листинг 6.14
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

# Создаём простую модель
# 4 входа, 4 скрытых нейрона, 1 выход
model = keras.Sequential([
    layers.Dense(4, activation='relu', input_shape=(4,)),
    layers.Dense(1, activation='linear')
])

# Компилируем модель (задаём оптимизатор и функцию потерь)
model.compile(optimizer='adam', loss='mean_squared_error')

# Входные данные для обучения (4 входных признака)
X_train = np.array([[2, 3, 80, 1],
                    [5, 5, 50, 2],
                    [10, 7, 40, 3],
                    [15, 9, 20, 4],
                    [20, 11, 10, 5]])
# Целевой выход (один на каждый входной признак)
y_train = np.array([5, 4, 3, 2, 1])

# Обучаем модель
history = model.fit(X_train, y_train, epochs=500, batch_size=1)

# Построение графика потерь (ошибок)
plt.plot(history.history['loss'])
plt.title('Потери модели')
plt.ylabel('Потери')
plt.xlabel('Эпохи')
plt.legend(['Учебные'], loc='upper left')
plt.show()

# Делаем предсказание на новых данных
# один образец с 4-мя признаками
X_test = np.array([[2, 3, 85, 1]])
prediction = model.predict(X_test)
print("На 5 (очень хорошая погода) - ", prediction)

X_test = np.array([[5, 4, 50, 2]])
prediction = model.predict(X_test)
print("На 4 (хорошая погода) - ", prediction)

X_test = np.array([[10, 7, 45, 3]])
prediction = model.predict(X_test)
print("На 3 (средняя погода) - ", prediction)

X_test = np.array([[15, 9, 21, 4]])
prediction = model.predict(X_test)
print("На 2 (плохая погода) - ", prediction)

X_test = np.array([[20, 11, 10, 6]])
prediction = model.predict(X_test)
print("На 1 (очень плохая погода) - ", prediction)