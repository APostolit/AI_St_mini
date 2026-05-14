# Листинг 8_10
import cv2
import os

# Инициализация детектора человека
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Текущий каталог
execution_path = os.getcwd()
# загрузка фотографии
img_path = execution_path + '/images/image_str.jpg'
image = cv2.imread(img_path)
cv2.imshow('Input photo', image)

# Обнаружение всех областей на изображении, где есть пешеходы
(regions, _) = hog.detectMultiScale(image, winStride=(4, 4),
                                    padding=(4, 4), scale=1.05)
# Рисование прямоугольников на изображении
for (x, y, w, h) in regions:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Отображение обработанного изображения
cv2.imshow("Image", image)
cv2.waitKey(0)  # Ожидание нажатия любой клавиши
cv2.destroyAllWindows()  # закрыть все окна