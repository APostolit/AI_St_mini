# Listing 7_19
from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = (execution_path +
              "/Im_Yolo_Trening/models/yolov3_Im_Yolo_Trening_mAP-0.70919_epoch-44.pt")
# Путь к файлу json
json_path = (execution_path +
             "/Im_Yolo_Trening/json/Im_Yolo_Trening_yolov3_detection_config.json")
# Путь к файлу с исходным изображением
img_in_path = execution_path + "/images/Znak_Zebra.jpg"
# Путь к файлу с обработанным изображением
im_out_path = execution_path + "/images/Znak_Zebra_New.jpg"

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.setJsonPath(json_path)
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=img_in_path,
                                             output_image_path=im_out_path,)
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"],
          " : ", detection["box_points"])

# Путь к файлу с исходным изображением
img_in_path = execution_path + "/images/Znak3.jpg"
# Путь к файлу с обработанным изображением
im_out_path = execution_path + "/images/Znak3_New.jpg"
detections = detector.detectObjectsFromImage(input_image=img_in_path,
                                             output_image_path=im_out_path,)
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"],
          " : ", detection["box_points"])