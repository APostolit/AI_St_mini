# Listing 7_17
from imageai.Detection.Custom import CustomVideoObjectDetection
import os

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = (execution_path +
              '/hololens-yolo/models/yolov3_hololens-yolo_mAP-0.82726_epoch-73.pt')
json_path = (execution_path +
             '/hololens-yolo/json/hololens-yolo_yolov3_detection_config.json')
# Путь к файлу с изображением
video_path_in = execution_path + '/video/holo1.mp4'
# Путь к обработанному файлу
video_path_out = execution_path + '/video/holo1-detected'

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(model_path)
video_detector.setJsonPath(json_path)
video_detector.loadModel()

video_detector.detectObjectsFromVideo(input_file_path=video_path_in,
                                      output_file_path=video_path_out,
                                      frames_per_second=30,
                                      minimum_percentage_probability=40,
                                      log_progress=True)
