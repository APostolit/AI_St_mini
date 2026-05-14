# Listing 7_11
from imageai.Detection import VideoObjectDetection
import os
import streamlit as st
from ffmpeg import FFmpeg

tab_1, tab_2, tab_3 = st.tabs(['Объекты', 'Исходное видео',
                               'Обработанное видео'])

def forFrame(frame_number, output_array, output_count):
    st.write("НОМЕР ФРЕЙМА ", frame_number)
    # st.write("Массив параметров найденных объектов: ", output_array)
    st.text("Количество найденных объектов: " + str(output_count))

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/yolov3.pt'

# Путь к файлу с видео
video_path_in = execution_path + '/video/transport.mp4'
# Путь к обработанном файлу с видео
video_path_out = execution_path +  '/video/video_frame_analysis'
# Путь записи файла с кодеком H264 для отображения в streamlit
video_path_analiz = execution_path +  '/video/video_frame_analysis.mp4'
video_path_h256 = execution_path + '/video/frame_analysis_h256.mp4'

execution_path = os.getcwd()
video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(model_path)
video_detector.loadModel()

with st.spinner(text="Ждите, идет обработка видео...", show_time=True):
    with tab_1:
        with st.container(height=500):
            video_detector.detectObjectsFromVideo(
                input_file_path=video_path_in,
                output_file_path=video_path_out,
                frames_per_second=20,
                per_frame_function=forFrame,
                minimum_percentage_probability=30)

# Перезапись обработанного файла для streamlit
with st.spinner(text="Ждите, идет кодировка видео...", show_time=True):
    ffmpeg = (
        FFmpeg()
        .option("y")  # Опция для подтверждения перезаписи файлов
        .input(video_path_analiz)    # Обработанный файл
        .output(video_path_h256,  # Перекодированный файл
                {"codec:v": "libx264"})  # Кодек видео H.264
    )
    ffmpeg.execute()

with tab_2:
    video_file_in = open(video_path_in, "rb")
    video_bytes_in = video_file_in.read()
    st.video(video_bytes_in, format="video/mp4")
with tab_3:
    video_file_out = open(video_path_h256, "rb")
    video_bytes_out = video_file_out.read()
    st.video(video_bytes_out, format="video/mp4")
