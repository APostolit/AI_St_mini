# Листинг 6.12
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Создание модели
model = Sequential()
model.add(Dense(2, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=SGD(learning_rate=0.1))

# Формирование обучающих данных
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Обучение сети
with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
    history = model.fit(X, y, batch_size=1, epochs=400, verbose=1)

# Построение графика потерь (ошибок)
plt.plot(history.history['loss'])
plt.title('Потери модели')
plt.ylabel('Потери')
plt.xlabel('Эпохи')
plt.legend(['Учебные'], loc='upper left')
st.pyplot(plt)

# Тестирование работы обученной сети
st.write("Проверка работы обученной сети:")
st.text("Для XOR(0,0) верное решение -0, получено:" +
      str(model.predict(np.array([[0, 0]]))))
st.text("Для XOR(0,1) верное решение -1, получено:" +
      str(model.predict(np.array([[0, 1]]))))
st.text("Для XOR(1,0) верное решение -1, получено:" +
      str(model.predict(np.array([[1, 0]]))))
st.text("Для XOR(1,1) верное решение -0, получено:" +
      str(model.predict(np.array([[1, 1]]))))

