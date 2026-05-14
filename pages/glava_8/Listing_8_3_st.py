# Listing 8_3
import cv2
import streamlit as st
import os

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'

# Путь к файлу с исходным изображением
img_path_in = execution_path + '/images/Test_Face_eye.jpg'
# Путь к файлу с обработанным изображением
img_path_out = execution_path + '/images/Test_Face_Eye_det.jpg'

tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])

# Загрузка изображения
img = cv2.imread(img_path_in)
# показать загруженное изображение
with tab_1:
    st.image(img, channels="BGR")

# Загрузка каскадов Хаара
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Выполнение распознавания лиц
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)  # распознавание глаз
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh),
                      (0, 255, 0), 2)

# сохранить изображение
cv2.imwrite(img_path_out, img)

# загрузка обработанного изображения
img = cv2.imread(img_path_out)
with tab_2:
    st.image(img, channels="BGR")