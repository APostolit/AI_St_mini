# Листинг 8_9
import cv2
import os

# Функция рисования прямоугольников
def my_box(img, bboxes):
    # формирование прямоугольника вокруг каждого обнаруженного объекта
    for box in bboxes:
        # формирование координат
        x, y, width, height = box
        x2, y2 = x + width, y + height
        # рисование прямоугольников
        cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 2)
    return img

# Текущий каталог
execution_path = os.getcwd()
# загрузка фотографии
img_path = execution_path + '/images/Test4.jpg'
img = cv2.imread(img_path)
cv2.imshow('Input photo', img)

# Все тело
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fullbody.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray, scaleFactor=1.2,
                                     minNeighbors=2, minSize=(30, 30))
img = my_box(img, bboxes)
cv2.imshow('Body', img)  # показать
cv2.waitKey(0)    # держать окно с изображением открытым

# Верхняя часть тела
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_upperbody.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray, scaleFactor=1.2,
                                     minNeighbors=4, minSize=(30, 30))
img = my_box(img, bboxes)
cv2.imshow('Upper body', img)  # показать
cv2.waitKey(0)    # держать окно с изображением открытым

# Нижняя часть тела
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_lowerbody.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray, scaleFactor=1.1,
                                     minNeighbors=2, minSize=(30, 30))
img = my_box(img, bboxes)
cv2.imshow('Lower body', img)  # показать
cv2.waitKey(0)    # держать окно с изображением открытым

# Правый глаз
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_righteye_2splits.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray)
img = my_box(img, bboxes)
cv2.imshow('Right eye', img)  # показать
cv2.waitKey(0)    # держать окно с изображением открытым

# Левый глаз
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")
# выполнение распознавания объектов
bboxes = classifier.detectMultiScale(gray)
img = my_box(img, bboxes)
cv2.imshow('Lef eye', img)  # показать
cv2.waitKey(0)    # держать окно с изображением открытым

cv2.destroyAllWindows()  # закрыть все окна