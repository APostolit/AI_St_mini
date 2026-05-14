# Листинг 6.13
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

t_1, t_2, t_3, t_4, t_5, t_6, t_7 = st.tabs(['Данные', 'Образец', 'Образцы',
                                             'Обучение', 'Прогноз 0', 'Прогноз 12',
                                             'Прогноз для группы'])

# Загрузка данных для обучения модели
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

with t_1:
    # Вывод сведений об исходном наборе данных
    Tr_Im = train_images.shape
    Tr_label = len(train_labels)
    Labels = train_labels
    st.write('Тренировочный массив изображений', Tr_Im)
    st.write('Тренировочный массив меток', Tr_label)
    st.text('Метки изображений' + str(Labels))

    Test_Im = test_images.shape
    Test_label = len(test_labels)
    st.write('Тестовый массив изображений', Test_Im)
    st.write('Тестовый массив меток', Test_label)

with t_2:
    col_1, col_2 = st.columns(2)
    with col_1:
        # Вывод изображения элемента с индексом 0
        plt.clf()  # Очистить график от предыдущих данных
        plt.figure()
        plt.imshow(train_images[0])
        plt.colorbar()
        plt.grid(False)
        st.pyplot(plt)

    # Масштабирование цветности изображений
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    with col_2:
        # Вывод изображения элемента с индексом 0
        plt.clf()  # Очистить график от предыдущих данных
        plt.figure()
        plt.imshow(train_images[0])
        plt.colorbar()
        plt.grid(False)
        st.pyplot(plt)

with t_3:
    # Вывод первых 25 элементов изображений из набора данных
    plt.clf()  # Очистить график от предыдущих данных
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    st.pyplot(plt)

# Создание модели
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')])
# Компиляция модели
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучение модели
with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
    history = model.fit(train_images, train_labels, epochs=10)

with t_4:
    # Построение графика потерь (ошибок)
    plt.clf()  # Очистить график от предыдущих данных
    plt.plot(history.history['loss'])
    plt.title('Потери модели')
    plt.ylabel('Потери')
    plt.xlabel('Эпохи')
    plt.legend(['Учебные'], loc='upper left')
    st.pyplot(plt)
    # Оценка точности модели после обучения
    test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    st.write('Точность на проверочных данных')
    st.write('test_loss= ', test_loss)
    st.write('test_acc= ', test_acc)

# Функция вывода изображения с результатами предсказания
def plot_image(i, predictions_array, true_label, img):
    global class_names
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.clf()  # Очистить график от предыдущих данных
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
       color = 'blue'
    else:
       color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                     100 * np.max(predictions_array),
                                     class_names[true_label]),
                                     color=color, fontsize=8)

# Функция вывода гистограммы с результатами предсказания
def plot_value_array(i, predictions_array, true_label):
    global class_names
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.clf()  # Очистить график от предыдущих данных
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    plt.xticks(range(10), class_names, rotation=45, fontsize=5)
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

# Оценка предсказания на элементе с индексом 0
predictions = model.predict(test_images)
ver1 = predictions[0]
im1 = np.argmax(predictions[0])
lab1 = test_labels[0]

# Преобразование данных от numpy к Python
ver1 = np.array(ver1, dtype=np.float64).tolist()
# Округление до 2-х знаков
ver1 = [round(elem, 2) for elem in ver1]

with t_5:
    # Итог предсказания для объекта с индексом 0
    i = 0
    col_3, col_4 = st.columns([1, 2])
    with col_3:
        plt.figure(figsize=(4, 2))
        plt.subplot(1, 2, 1)
        plot_image(i, predictions, test_labels, test_images)
        st.pyplot(plt)
    with col_4:
        plt.subplot(1, 2, 2)
        plot_value_array(i, predictions, test_labels)
        st.pyplot(plt)
        st.text('Вероятность предсказаний:')
        st.text(ver1)
        st.write('Распознан объект: ', class_names[im1])
        st.write('Метка объекта: ', lab1)

# Оценка предсказания на элементе с индексом 12
predictions = model.predict(test_images)
ver1 = predictions[12]
im1 = np.argmax(predictions[12])
lab1 = test_labels[12]

# Преобразование данных от numpy к Python
ver1 = np.array(ver1, dtype=np.float64).tolist()
# Округление до 2-х знаков
ver1 = [round(elem, 2) for elem in ver1]
with t_6:
    # Итог предсказания для объекта с индексом 12
    i = 12
    col_5, col_6 = st.columns([1, 2])
    with col_5:
        plt.figure(figsize=(4, 2))
        plt.subplot(1, 2, 1)
        plot_image(i, predictions, test_labels, test_images)
        st.pyplot(plt)
    with col_6:
        plt.subplot(1, 2, 2)
        plot_value_array(i, predictions, test_labels)
        st.pyplot(plt)
        st.text('Вероятность предсказаний:')
        st.text(ver1)
        st.write('Распознан объект: ', class_names[im1])
        st.write('Метка объекта: ', lab1)

# Отображаем первые X тестовых изображений, их предсказанную и настоящую метки.
# Корректные предсказания окрашиваем в синий цвет, ошибочные — в красный.
num_images = 6
with t_7:
    plt.clf()  # Очистить график от предыдущих данных
    for i in range(num_images):
        col_5, col_6 = st.columns([1, 2])
        with col_5:
            plt.figure(figsize=(4, 2))
            plt.subplot(1, 2, 1)
            plot_image(i, predictions, test_labels, test_images)
            st.pyplot(plt)
        with col_6:
            plt.subplot(1, 2, 2)
            plot_value_array(i, predictions, test_labels, )
            st.pyplot(plt)