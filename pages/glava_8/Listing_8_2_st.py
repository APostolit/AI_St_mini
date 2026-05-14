# Listing 8_2
import cv2
import streamlit as st

# загрузка каскада Хаара
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

st.session_state.stream = True
tab1, tab2 = st.tabs(['Камера', 'Stop'])

with tab1:
    try:
        # Активация встроенной видеокамеры
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
                # Захват кадр за кадром
                ret, frame = cam.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray,
                                                     scaleFactor=1.1,
                                                     minNeighbors=5,
                                                     minSize=(30, 30),
                                                     flags=cv2.CASCADE_SCALE_IMAGE)
                # Рисование прямоугольников вокруг лиц
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Показ обработанного кадра
                frame_placeholder.image(frame, channels="BGR")
    except Exception as e:
        st.write('Отсутствует камера')