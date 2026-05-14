# Листинг 6.12
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt

# Создание модели
model = Sequential()
model.add(Dense(2, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.1))
# print(model.summary())

# Формирование обучающих данных
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Обучение сети
history = model.fit(X, y, batch_size=1, epochs=400, verbose=1)

# Построение графика потерь (ошибок)
plt.plot(history.history['loss'])
plt.title('Потери модели')
plt.ylabel('Потери')
plt.xlabel('Эпохи')
plt.legend(['Учебные'], loc='upper left')
plt.show()

# Тестирование работы обученной сети
print("Проверка работы обученной сети:")
print("Для XOR(0,0) верное решение -0, получено:",
      model.predict(np.array([[0, 0]])))
print("Для XOR(0,1) верное решение -1, получено:",
      model.predict(np.array([[0, 1]])))
print("Для XOR(1,0) верное решение -1, получено:",
      model.predict(np.array([[1, 0]])))
print("Для XOR(1,1) верное решение -0, получено:",
      model.predict(np.array([[1, 1]])))