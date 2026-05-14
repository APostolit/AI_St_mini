from imageai.Detection import ObjectDetection
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

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

# Вывод результатов обнаружения
tab_1, tab_2, tab_3 = st.tabs(['Исходное изображение',
                               'Обнаруженные объекты',
                               'Обработанное изображение'])
with tab_1:
    st.image(img_path_in)
with tab_2:
    for eachObject in detections:
        st.text(eachObject["name"]+": "+
                str(eachObject["percentage_probability"])+": "+
                str(eachObject["box_points"]))
with tab_3:
    st.image(img_path_out)