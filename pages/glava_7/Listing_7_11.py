# Listing 7_11
from imageai.Detection import VideoObjectDetection
import os

def forFrame(frame_number, output_array, output_count):
    print("НОМЕР ФРЕЙМА ", frame_number)
    print("Массив параметров найденных объектов: ", output_array)
    print("Количество найденных объектов: ", output_count)
    print("------------КОНЕЦ ФРЕЙМА --------------")

execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = execution_path + '/models/yolov3.pt'
# Путь к файлу с видео
video_path_in = execution_path + '/video/transport.mp4'
video_path_out = execution_path +  '/video/video_frame_analysis'

execution_path = os.getcwd()
video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(model_path)
video_detector.loadModel()

video_detector.detectObjectsFromVideo(
    input_file_path=video_path_in,
    output_file_path=video_path_out,
    frames_per_second=20,
    per_frame_function=forFrame,
    minimum_percentage_probability=30)