# Листинг 8_12
import cv2
import os
import numpy as np
from PIL import Image

def get_images(path):
    # Текущий каталог
    execution_path = os.getcwd()
    # Путь к фотографиям
    path_user = execution_path + '/DataSet1/user_'
    # Ищем все фотографии и записываем их в image_paths
    image_paths = [os.path.join(path, f)
                   for f in os.listdir(path) if not f.endswith('.happy')]

    count = 0
    images = []
    labels = []

    for image_path in image_paths:
        # Переводим изображение в черно-белый формат и приводим его
        # к формату массива
        gray = Image.open(image_path).convert('L')
        image = np.array(gray, 'uint8')
        # Из каждого имени файла извлекаем номер человека,
        # изображенного на фото
        subject_number = int(os.path.split(
            image_path)[1].split(".")[0].replace("subject", ""))

        # Определяем области, где есть лица
        faces = faceCascade.detectMultiScale(image, scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(30, 30))
        # Если лицо нашлось, добавляем его в список images,
        # а соответствующий ему номер — в список labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(subject_number)
            # В окне показываем изображение
            cv2.imshow("", image[y: y + h, x: x + w])
            cv2.waitKey(50)
            count += 1
            # Путь к сохраняемому файлу
            path_person = path_user + str(subject_number) + '_' + str(count) + '.jpg'
            # Сохраняем лицо
            cv2.imwrite(path_person, image[y: y + h, x: x + w])
    return images, labels

# Загрузка каскадов Хаара для поиска лиц
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Формирование локального бинарного шаблона
recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 123)

# Текущий каталог
execution_path = os.getcwd()
# Путь к фотографиям
path = execution_path + '/YaleFace/yalefaces/'
# Путь обученной модели
path_model = execution_path + '/YaleFace/Yale_face2.yml'

# Получаем лица и соответствующие им номера
images, labels = get_images(path)
cv2.destroyAllWindows()

# Обучаем программу распознавать лица
recognizer.train(images, np.array(labels))
# Сохраняем результат тренировки
recognizer.write(path_model)
print('Обучение закончено')
