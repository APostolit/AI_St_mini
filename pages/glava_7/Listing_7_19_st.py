# Listing 7_19
from imageai.Detection.Custom import CustomObjectDetection
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

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

tab_1, tab_2 = st.tabs(['Изображение 1', 'Изображение 2'])
with tab_1:
    col1, col2 = st.columns(2)
    with col1:
        st.image(img_in_path)
    with col2:
        st.image(im_out_path)
        for detection in detections:
           st.text(detection["name"]+ " : "+ str(detection["percentage_probability"])+
                  " : "+ str(detection["box_points"]))

# Путь к файлу с исходным изображением
img_in_path = execution_path + "/images/Znak3.jpg"
# Путь к файлу с обработанным изображением
im_out_path = execution_path + "/images/Znak3_New.jpg"
detections = detector.detectObjectsFromImage(input_image=img_in_path,
                                             output_image_path=im_out_path,)

with tab_2:
    col3, col4 = st.columns(2)
    with col3:
        st.image(img_in_path)
    with col4:
        st.image(im_out_path)
        for detection in detections:
            st.text(detection["name"] + " : " + str(detection["percentage_probability"]) +
                    " : " + str(detection["box_points"]))