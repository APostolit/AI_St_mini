# Listing 7_9
from imageai.Detection import VideoObjectDetection
import os
import streamlit as st
from ffmpeg import FFmpeg

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/tiny-yolov3.pt'
# Путь к файлу с видео
vide_path_in = execution_path + '/video/transport.mp4'
vide_path_out = execution_path +  '/video/transport_detected_1'

detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

with st.spinner(text="Ждите, идет обработка видео...", show_time=True):
    video_path = detector.detectObjectsFromVideo(
        input_file_path=vide_path_in,
        output_file_path=vide_path_out,
        frames_per_second=20,
        log_progress=True)

# Путь к обработанному файлу
video_path_detect = execution_path + '/video/transport_detected_1.mp4'
# Путь записи файла с кодеком H264 для отображения в streamlit
video_path_h256 = execution_path + '/video/detected_h256_1.mp4'

# Перезапись обработанного файла для streamlit
with st.spinner(text="Ждите, идет кодировка видео...", show_time=True):
    ffmpeg = (
        FFmpeg()
        .option("y")  # Опция для подтверждения перезаписи файлов
        .input(video_path_detect)  # Входной файл
        .output(video_path_h256,  # Выходной файл
                {"codec:v": "libx264"})  # Кодек видео H.264
    )
    ffmpeg.execute()

# Вывод результатов обнаружения
tab_1, tab_2 = st.tabs(['Исходное видео',
                        'Обработанное видео'])
with tab_1:
    video_file_in = open(vide_path_in, "rb")
    video_bytes_in = video_file_in.read()
    st.video(video_bytes_in, format="video/mp4")
with tab_2:
    video_file_out = open(video_path_h256, "rb")
    video_bytes_out = video_file_out.read()
    st.video(video_bytes_out, format="video/mp4")