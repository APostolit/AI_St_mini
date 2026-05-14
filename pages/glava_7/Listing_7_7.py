# Listing 7_7
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = execution_path + '/models/yolov3.pt'
# Путь к файлу с изображением
img_path_in = execution_path + '/images/image_str.jpg'
img_path_out = execution_path +  '/images/image_str_out.jpg'

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detections = detector.detectObjectsFromImage(
    input_image=img_path_in,
    output_image_path=img_path_out,
    minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"],
          " : ", eachObject["box_points"])
    print("--------------------------------")