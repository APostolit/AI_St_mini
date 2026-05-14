# Listing 7_17
from imageai.Detection.Custom import CustomVideoObjectDetection
import os
import streamlit as st
from ffmpeg import FFmpeg

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = (execution_path +
              '/hololens-yolo/models/yolov3_hololens-yolo_mAP-0.82726_epoch-73.pt')
json_path = (execution_path +
             '/hololens-yolo/json/hololens-yolo_yolov3_detection_config.json')
# Путь к файлу с изображением
video_path_in = execution_path + '/video/holo1.mp4'
# Путь к обработанному файлу
video_path_out = execution_path + '/video/holo1-detected'
# Путь записи файла с кодеком H264 для отображения в streamlit
video_path_analiz = execution_path +  '/video/holo1-detected.mp4'
video_path_h256 = execution_path + '/video/holo1-detected_h256.mp4'

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(model_path)
video_detector.setJsonPath(json_path)
video_detector.loadModel()

'''
video_detector.detectObjectsFromVideo(input_file_path=video_path_in,
                                      output_file_path=video_path_out,
                                      frames_per_second=30,
                                      minimum_percentage_probability=40,
                                      log_progress=True)
'''
# Перезапись обработанного файла для streamlit
with st.spinner(text="Ждите, идет кодировка видео...", show_time=True):
    ffmpeg = (
        FFmpeg()
        .option("y")  # Опция для подтверждения перезаписи файлов
        .input(video_path_analiz)    # Обработанный файл
        .output(video_path_h256,     # Перекодированный файл
                {"codec:v": "libx264"})  # Кодек видео H.264
    )
    ffmpeg.execute()

tab_1, tab_2 = st.tabs(['Исходное видео', 'Обработанное видео'])
with tab_1:
    st.video(video_path_in)
with tab_2:
    st.video(video_path_h256)