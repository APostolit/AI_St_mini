# Listing 8_4
import cv2
import streamlit as st
import os

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'

# Путь к файлу с исходным изображением
img_path_in = execution_path + '/images/smile.jpg'
# Путь к файлу с обработанным изображением
img_path_out = execution_path + '/images/smile_det.jpg'

# Загрузка входного изображения
img = cv2.imread(img_path_in)

tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
# показать загруженное изображение
with tab_1:
    st.image(img, channels="BGR")

# Преобразование в оттенки серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Загрузка каскадов Хаара
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      "haarcascade_smile.xml")

# Обнаружение лиц
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Обработка каждой обнаруженной лица
for (x, y, w, h) in faces:
    # Определение области интереса (ROI) для лица
    roi_gray = gray[y:y + h, x:x + w]

    # Обнаружение улыбок в области лица
    smiles = smile_cascade.detectMultiScale(roi_gray,
                                            1.8,
                                            20)

    if len(smiles) > 0:
        for (sx, sy, sw, sh) in smiles:
            # Рисование прямоугольника вокруг улыбки
            cv2.rectangle(img, (x + sx, y + sy),
                          (x + sx + sw, y + sy + sh), (0, 0, 255), 2)

# сохранить изображение
cv2.imwrite(img_path_out, img)

# загрузка обработанного изображения
img = cv2.imread(img_path_out)
with tab_2:
    st.image(img, channels="BGR")