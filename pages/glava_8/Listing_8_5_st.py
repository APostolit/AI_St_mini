# Listing 8_5
import cv2
import streamlit as st
import os

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'

# Путь к файлу с исходным изображением
img_path_in = execution_path + '/images/Test_Numer.jpg'
# Путь к файлу с обработанным изображением
img_path_out = execution_path + '/images/Test_Numer_det.jpg'

tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])

# Загрузка изображения
img = cv2.imread(img_path_in)
# показать загруженное изображение
with tab_1:
    st.image(img, channels="BGR")

# загрузка каскада Хаара
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
# Выполнение распознавания объектов
bboxes = classifier.detectMultiScale(img)
# формирование прямоугольника вокруг каждого обнаруженного объекта
for box in bboxes:
    # формирование координат
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # рисование прямоугольников
    cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 3)

cv2.imwrite(img_path_out, img)  # сохранить изображение

# загрузка обработанного изображения
img = cv2.imread(img_path_out)
with tab_2:
    st.image(img, channels="BGR")