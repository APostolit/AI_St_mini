# Listing 7_16
from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = (execution_path +
              '/hololens-yolo/models/yolov3_hololens-yolo_mAP-0.82726_epoch-73.pt')
json_path = (execution_path +
             '/hololens-yolo/json/hololens-yolo_yolov3_detection_config.json')
# Путь к файлу с изображением
img_path_in = execution_path + '/images/holo1.jpg'
# Путь к обработанному файлу
img_path_out = execution_path + '/images/holo1-detected.jpg'


detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.setJsonPath(json_path)
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=img_path_in,
                                             output_image_path=img_path_out)
print('Изображение 1')
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"],
          " : ", detection["box_points"])

# Путь к файлу с изображением
img_path_in = execution_path + '/images/holo2.jpg'
# Путь к обработанному файлу
img_path_out = execution_path + '/images/holo2-detected.jpg'
detections = detector.detectObjectsFromImage(input_image=img_path_in,
                                             output_image_path=img_path_out)
print('Изображение 2')
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"],
          " : ", detection["box_points"])