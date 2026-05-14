# Listing 8_5
import cv2
import os
# Текущий каталог
execution_path = os.getcwd()
# Путь к файлу с исходным изображением
img_path_in = execution_path + '/images/Test_Numer.jpg'
# Путь к файлу с обработанным изображением
img_path_out = execution_path + '/images/Test_Numer_det.jpg'

# Загрузка изображения
img = cv2.imread(img_path_in)
# показать загруженное изображение
cv2.imshow('Input photo', img)
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

cv2.imshow('Window with object detection', img)  # показать изображение
cv2.imwrite(img_path_out, img)  # сохранить изображение

cv2.waitKey(0)  # держать окно с изображениями открытым
cv2.destroyAllWindows()   # закрыть все окна