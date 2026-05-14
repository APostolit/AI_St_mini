# Listing 8_3
import cv2
import os

# Текущий каталог
execution_path = os.getcwd()
# Путь к файлу с исходным изображением
img_path_in = execution_path + '/images/Test_Face_eye.jpg'
# Путь к файлу с обработанным изображением
img_path_out = execution_path + '/images/Test_Face_Eye_det.jpg'

# Загрузка изображения
img = cv2.imread(img_path_in)
# показать загруженное изображение
cv2.imshow('Input photo', img)
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

cv2.imshow('Out photo', img)  # показать обработанное изображение
cv2.imwrite(img_path_out, img)  # сохранить изображение

cv2.waitKey(0)  # держать окно с изображением открытым
cv2.destroyAllWindows()  # закрыть все окна