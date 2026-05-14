# Listing 7_6
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = execution_path + '/models/retinanet_resnet50_fpn_coco-eeacb38b.pth'
# Путь к файлу с изображением
img_path_in = execution_path + '/images/image5.jpg'
img_path_out = execution_path + '/images/image52.jpg'

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(model_path)
# Загрузка модели
detector.loadModel()
# Задать тип объекта для обнаружения
custom = detector.CustomObjects(person=True, dog=True)
# Обнаружение объектов на изображении
detections = detector.detectObjectsFromImage(
    custom_objects=custom,
    input_image=img_path_in,
    output_image_path=img_path_out,
    minimum_percentage_probability=30)
# Вывод результатов обнаружения
for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"],
          " : ", eachObject["box_points"])
    print("--------------------------------")