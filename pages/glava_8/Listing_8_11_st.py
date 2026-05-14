# Листинг 8_11
import cv2
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'
video_path = execution_path + '/video/Person.mp4'

# Инициализация детектора человека
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# Загрузка видеофайла
cap = cv2.VideoCapture(video_path)

# Создание placeholder для отображения кадра
frame_placeholder = st.empty()

while cap.isOpened():
    # Чтение видеопотока
    ret, image = cap.read()
    if ret:
        image = cv2.resize(image, None, fx=0.5, fy=0.5,
                           interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Обнаружение бластей, в которых есть пешеходы
        (regions, _) = hog.detectMultiScale(gray, winStride=(4, 4),
                                            padding=(4, 4), scale=1.5)

        # Рисование прямоугольников на изображении
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Показ обработанного кадра
        frame_placeholder.image(image, channels="BGR")