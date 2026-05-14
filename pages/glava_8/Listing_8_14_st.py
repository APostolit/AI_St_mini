# Листинг 8_14
import cv2
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'

# Путь к фотографиям
path = execution_path + '/DataSet/user.'
# Создаем детектор лица
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

try:
    # Активируем камеру
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)

    # Вводим id лица, которое добавляется в имя и потом будет
    # использоваться при распознавании.
    face_id = "Mark"
    st.write("Захват лица. Смотрите в камеру и ждите...")
    # Создание placeholder для отображения кадра
    frame_placeholder = st.empty()
    count = 0
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1
            # Сохраняем лицо
            cv2.imwrite(path + str(face_id) + '.' +
                        str(count) + '.jpg',  gray[y:y+h, x:x+w])
        # Показ обработанного кадра
        frame_placeholder.image(img, channels="BGR")
        # cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff  # Выход - 'ESC'
        if k == 27:
            break
        elif count >= 30:  # Если сохранили 30 изображений - выход
            break
    st.write("Программа завершена")
except Exception as e:
    st.write('Отсутствует камера')