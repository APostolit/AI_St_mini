# Listing 7_10
from imageai.Detection import ObjectDetection
import os
import cv2
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/yolov3.pt'
# Загрузка модели
obj_detect = ObjectDetection()
obj_detect.setModelTypeAsYOLOv3()
obj_detect.setModelPath(model_path)
obj_detect.loadModel()

st.session_state.stream = True

tab1, tab2 = st.tabs(['Камера', 'Stop'])

with tab1:
    try:
        # Инициализация видео камеры
        cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)
        with tab2:
            bt_stop = st.button('Stop', type="primary")
            if bt_stop:
                st.session_state.stream = False
                # Освобождение камеры
                cam.release()
                cv2.destroyAllWindows()

        # Создание placeholder для отображения кадра
        frame_placeholder = st.empty()
        if st.session_state.stream == True:
            # Запуск цикла обработки кадров видео камеры
            while True:
                ret, img = cam.read()
                # Распознавание объектов в кадре
                annotated_image, preds = obj_detect.detectObjectsFromImage(input_image=img,
                                                                           output_type="array",
                                                                           display_percentage_probability=True,
                                                                           display_object_name=True)
                # Отобразить текущий кадр
                frame_placeholder.image(annotated_image, channels="BGR")
    except Exception as e:
        st.write('Отсутствует камера')