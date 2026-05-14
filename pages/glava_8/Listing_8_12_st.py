# Листинг 8_12
import cv2
import os
import numpy as np
from PIL import Image
import streamlit as st
import time

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'
# Путь к фотографиям
path = execution_path + '/YaleFace/yalefaces/'
# Путь обученной модели
path_model = execution_path + '/YaleFace/Yale_face2.yml'

# Загрузка каскадов Хаара для поиска лиц
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Формирование локального бинарного шаблона
recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 123)

def get_images(path):
    # Текущий каталог
    global execution_path, faceCascade
    # Создание placeholder для отображения кадра
    frame_placeholder = st.empty()
    # Ищем все фотографии и записываем их в image_paths
    image_paths = [os.path.join(path, f)
                   for f in os.listdir(path) if not f.endswith('.happy')]

    images = []
    labels = []

    for image_path in image_paths:
        # Переводим изображение в черно-белый формат и приводим его
        # к формату массива
        gray = Image.open(image_path).convert('L')
        # st.image(gray)
        image = np.array(gray, 'uint8')
        # Из каждого имени файла извлекаем номер человека,
        # изображенного на фото
        subject_number = int(os.path.split(
            image_path)[1].split(".")[0].replace("subject", ""))

        # Определяем области, где есть лица
        faces = faceCascade.detectMultiScale(image, scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(30, 30))
        # Если лицо нашлось, добавляем его в список images,
        # а соответствующий ему номер — в список labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(subject_number)
            # Показ обработанного кадра
            frame_placeholder.image(image)
            time.sleep(0.05)
    return images, labels

# Получаем лица и соответствующие им номера
with st.spinner(text="Ждите, идет процесс извлечения фото...", show_time=True):
    images, labels = get_images(path)

# Обучаем программу распознавать лица
with st.spinner(text="Ждите, идет процесс обучения...", show_time=True):
    recognizer.train(images, np.array(labels))
    # Сохраняем результат тренировки
    recognizer.write(path_model)
    st.write('Обучение закончено')