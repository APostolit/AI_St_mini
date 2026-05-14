# Listing 7_16
from imageai.Detection.Custom import CustomObjectDetection
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

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

tab_1, tab_2 = st.tabs(['Изображение 1', 'Изображение 2'])
with tab_1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write('Исходное изображение')
        st.image(img_path_in)
        for detection in detections:
            st.text(detection["name"] + " : " +
                    str(detection["percentage_probability"]) + " : " +
                    str(detection["box_points"]))
    with col2:
        st.write('Обработанное изображение')
        st.image(img_path_out)



# Путь к файлу с изображением
img_path_in = execution_path + '/images/holo2.jpg'
# Путь к обработанному файлу
img_path_out = execution_path + '/images/holo2-detected.jpg'
detections = detector.detectObjectsFromImage(input_image=img_path_in,
                                             output_image_path=img_path_out)
with tab_2:
    col3, col4 = st.columns(2)
    with col3:
        st.write('Исходное изображение')
        st.image(img_path_in)
    with col4:
        st.write('Обработанное изображение')
        st.image(img_path_out)
    for detection in detections:
        st.text(detection["name"] + " : " +
                str(detection["percentage_probability"]) + " : " +
                str(detection["box_points"]))