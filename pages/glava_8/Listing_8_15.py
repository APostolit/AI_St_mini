# Листинг 8_15
import cv2
import numpy as np
import os

# Текущий каталог
execution_path = os.getcwd()
# Путь к папке с набором тренировочных фото
path = execution_path + '/DataSet/'
# Путь обученной модели
path_model = execution_path + '/Mark_model/face_Mark.yml'

recognizer = cv2.face.LBPHFaceRecognizer_create()

# Функция чтения изображений из папки с тренировочными фото
def getImagesAndLabels(path):
    # Создаем список файлов в папке patch
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    face = []  # тут храним массив картинок
    ids = []  # храним id лица
    for imagePath in imagePaths:
        img = cv2.imread(imagePath)
        # Переводим изображение, тренер принимает изображения
        # в оттенках серого
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face.append(img)  # записываем тренировочное фото в массив
        # Получаем id фото из его названия
        id = int(os.path.split(imagePath)[-1].split(".")[2])
        ids.append(id)  # записываем id тренировочного фото в массив
    return face, ids

# Чтение тренировочного набора фотографий из папки path
faces, ids = getImagesAndLabels(path)
# Тренируем модель распознавания
recognizer.train(faces, np.array(ids))
# Сохраняем результат тренировки
recognizer.write(path_model)