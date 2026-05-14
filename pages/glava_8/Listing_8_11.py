# Листинг 8_11
import cv2
import os

# Текущий каталог
execution_path = os.getcwd()
video_path = execution_path + '/video/Person.mp4'

# Инициализация детектора человека
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# Загрузка видеофайла
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    # Чтение видеопотока
    ret, image = cap.read()
    if ret:
        image = cv2.resize(image, None, fx=0.5, fy=0.5,
                           interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Обнаружение всех областей на изображении,
        #  в которых есть пешеходы
        (regions, _) = hog.detectMultiScale(gray, winStride=(4, 4),
                                            padding=(4, 4), scale=1.5)

        # Рисование прямоугольников на изображении
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Video", image) # показ видео
        # завершить, если нажата клавиша Esc
        if cv2.waitKey(33) == 27:
            break
    else:
        break
