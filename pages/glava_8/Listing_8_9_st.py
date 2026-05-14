# Листинг 8_9
import cv2
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'
# Вкладки
t1, t2, t3, t4, t5, t6 = st.tabs(['Изображение', 'Все тело',
                                  'Верх тела', 'Низ тела',
                                  'Правый глаз', 'Левый глаз'])

# загрузка фотографии
img_path = execution_path + '/images/Test4.jpg'
img = cv2.imread(img_path)
with t1:
    st.image(img,channels="BGR")

# Все тело
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray, scaleFactor=1.2,
                                     minNeighbors=2, minSize=(30, 30))
# формирование прямоугольника вокруг каждого обнаруженного объекта
for box in bboxes:
    # формирование координат
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # рисование прямоугольников
    cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
with t2:
    st.image(img,channels="BGR")

# Верхняя часть тела
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_upperbody.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray, scaleFactor=1.2,
                                     minNeighbors=4, minSize=(30, 30))
# формирование прямоугольника вокруг каждого обнаруженного объекта
for box in bboxes:
    # формирование координат
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # рисование прямоугольников
    cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
with t3:
    st.image(img,channels="BGR")

# Нижняя часть тела
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_lowerbody.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray, scaleFactor=1.1,
                                     minNeighbors=2, minSize=(30, 30))
# формирование прямоугольника вокруг каждого обнаруженного объекта
for box in bboxes:
    # формирование координат
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # рисование прямоугольников
    cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
with t4:
    st.image(img,channels="BGR")

# Правый глаз
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray)
# формирование прямоугольника вокруг каждого обнаруженного объекта
for box in bboxes:
    # формирование координат
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # рисование прямоугольников
    cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
with t5:
    st.image(img,channels="BGR")

# Левый глаз
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray)
# формирование прямоугольника вокруг каждого обнаруженного объекта
for box in bboxes:
    # формирование координат
    x, y, width, height = box
    x2, y2 = x + width, y + height
    # рисование прямоугольников
    cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
with t6:
    st.image(img,channels="BGR")