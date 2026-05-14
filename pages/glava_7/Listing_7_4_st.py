# Listing 7_4
from imageai.Detection import ObjectDetection
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/yolov3.pt'
# Путь к файлу с изображением
img_path_in = execution_path + '/images/image5.jpg'
img_path_out = execution_path + '/images/image_out5.jpg'

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
# Загрузка модели
detector.loadModel()
# Обнаружение объектов на изображении
detections = detector.detectObjectsFromImage(
    input_image=img_path_in,
    output_image_path=img_path_out,
    minimum_percentage_probability=30)

# Вывод результатов обнаружения
col_1, col_2 = st.columns([1,3])
with col_1:
    for eachObject in detections:
        st.write(eachObject["name"], " : ", eachObject["percentage_probability"])
        st.text(eachObject["box_points"])
        st.write("--------------------------------")
with col_2:
    tab_1, tab_2 = st.tabs(['Исходное изображение','Обработанное изображение'])
    with tab_1:
        st.image(img_path_in)
    with tab_2:
        st.image(img_path_out)