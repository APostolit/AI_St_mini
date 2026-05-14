# Листинг 8_10
import cv2
import os
import streamlit as st

# Инициализация детектора человека
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'
# Вкладки
t1, t2 = st.tabs(['Исходное изображение',
                  'Обработанное изображение'])
# загрузка фотографии
img_path = execution_path + '/images/image_str.jpg'
image = cv2.imread(img_path)
with t1:
    st.image(image, channels="BGR")

# Обнаружение всех областей на изображении, где есть пешеходы
(regions, _) = hog.detectMultiScale(image, winStride=(4, 4),
                                    padding=(4, 4), scale=1.05)
# Рисование прямоугольников на изображении
for (x, y, w, h) in regions:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Отображение обработанного изображения
with t2:
    st.image(image,channels="BGR")