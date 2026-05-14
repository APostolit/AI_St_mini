# Листинг 6.11
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import streamlit as st
from keras.models import load_model
np.random.seed(123)

tab_1, tab_2 = st.tabs(['Точность модели', 'Потери модели'])

# Загрузка исходных данных
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# Трансформация изображений в оттенки серого
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

# Кодирование значений меток нулями и единицами
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Создание модели
model = Sequential()
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D())
model.add(Conv2D(128, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='sgd', loss='mean_squared_error',  metrics=['accuracy'])

with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5)

# Построение графика точности предсказания
plt.clf()  # Очистить график от предыдущих данных
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Точность модели')
plt.ylabel('Точность')
plt.xlabel('Эпохи')
plt.legend(['Учебные', 'Тестовые'], loc='best')
with tab_1:
    st.pyplot(plt)

# Построение графика потерь (ошибок)
plt.clf()  # Очистить график от предыдущих данных
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Потери модели')
plt.ylabel('Потери')
plt.xlabel('Эпохи')
plt.legend(['Учебные', 'Тестовые'], loc='best')
with tab_2:
    st.pyplot(plt)

# Запись обученной модели сети в файл my_model.h5
model.save('my_model.h5')
# Удаление модели
del model
# Загрузка обученной модели сети из файла
model_New = load_model('my_model.h5')
y_predict = np.argmax(model_New.predict(X_train[:3]), axis=-1)
st.write('Первые 3 цифры')
st.text(y_train[:3])
st.text('Первые 3 предсказания: ' + str(y_predict))