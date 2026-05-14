# Listing 7_10
from imageai.Detection import ObjectDetection
import os
import cv2

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = execution_path + '/models/yolov3.pt'
# Загрузка модели
obj_detect = ObjectDetection()
obj_detect.setModelTypeAsYOLOv3()
obj_detect.setModelPath(model_path)
obj_detect.loadModel()

try:
    # Инициализация видео камеры
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)

    # Запуск цикла обработки кадров видео камеры
    while True:
        ret, img = cam.read()
        # Распознавание объектов в кадре
        annotated_image, preds = obj_detect.detectObjectsFromImage(
            input_image=img,
            output_type="array",
            display_percentage_probability=True,
            display_object_name=True)
        # Отобразить текущий кадр
        cv2.imshow("Window", annotated_image)
        # Прерывание трансляции с камеры
        if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1) == 27):
            break
    # Освобождение камеры
    cam.release()
    cv2.destroyAllWindows()
except Exception as e:
    print('Отсутствует камера')