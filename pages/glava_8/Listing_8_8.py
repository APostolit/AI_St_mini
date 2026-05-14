# Листинг 8_8
import cv2
import os

# Текущий каталог
execution_path = os.getcwd()

# активация камеры
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # активация камеры
# Путь к файлу с каскадами Хаара
path_cascade = execution_path + '/XML/cars.xml'
# загрузка классификатора
car_cascade = cv2.CascadeClassifier(path_cascade)
print(car_cascade)

# цикл обработки кадров
while True:
    ret, frames = cap.read()  # читает кадры из видео
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)    # оттенки серого
    # обнаруживает автомобили
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    # Нарисовать прямоугольник в найденном авто
    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # отображать обработанные кадры в окне
    cv2.imshow('video', frames)
    # завершить, если нажата клавиша Esc
    if cv2.waitKey(33) == 27:
        break
