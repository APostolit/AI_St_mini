# Листинг 8_16
import cv2
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'
# Путь обученной модели
path_model = execution_path + '/Mark_model/face_Mark.yml'

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(path_model)

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Тип шрифта
font = cv2.FONT_HERSHEY_SIMPLEX

# Список имен для id
names = ['None', 'Mark']

st.session_state.stream = True
tab1, tab2 = st.tabs(['Камера', 'Stop'])

with tab1:
    try:
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # размер видео кадра – ширина
        cam.set(4, 480)  # размер видео кадра – высота

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
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2,
                    minNeighbors=5, minSize=(10, 10),)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                    # Проверяем, что лицо распознано
                    if (confidence < 100):
                        id_obj = names[1]
                        confidence = "  {0}%".format(round(100 - confidence))
                    else:
                        id_obj = names[0]
                        confidence = "  {0}%".format(round(100 - confidence))

                    cv2.putText(img, str(id_obj), (x + 5, y - 5),
                                font, 1, (255, 255, 255), 2)
                    cv2.putText(img, str(confidence), (x + 5, y + h - 5),
                                font, 1, (255, 255, 0), 1)

                # cv2.imshow('camera', img)
                # Показ обработанного кадра
                frame_placeholder.image(img, channels="BGR")
    except Exception as e:
        st.write('Отсутствует камера')