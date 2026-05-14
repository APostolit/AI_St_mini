# Листинг 8_7
import cv2
import os

# Текущий каталог
execution_path = os.getcwd()
# Путь к файлу с исходным изображением
img_path_znak = execution_path + '/images/znak.jpg'
# Путь к файлу с обработанным изображением
img_path_avto_znak = execution_path + '/images/avto_znak.jpg'

classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

# Вариант активации камеры
# video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Активация камеры
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # градация серого
    plaques = classifier.detectMultiScale(gray, 1.3, 5)
    for i, (x, y, w, h) in enumerate(plaques):
        roi_color = frame[y:y + h, x:x + w]
        cv2.putText(frame,
                    str(x) + " " + str(y) + " " + str(w) + " " + str(h),
                   (480, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                   (255, 255, 255))
        r = 400.0 / roi_color.shape[1]
        dim = (400, int(roi_color.shape[0] * r))
        resized = cv2.resize(roi_color, dim,
                             interpolation=cv2.INTER_AREA)
        w_resized = resized.shape[0]
        h_resized = resized.shape[1]
        # Собираем в основную картинку
        frame[100:100 + w_resized, 100:100 + h_resized] = resized
        cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            # сохранить только знак
            cv2.imwrite(img_path_znak, resized)

    # Отображение результирующего кадра
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('v'):
        # сохранить автомобиль и знак
        cv2.imwrite(img_path_avto_znak, frame)

    # завершить, если нажата клавиша Esc
    if cv2.waitKey(33) == 27:
        break

# деактивировать камеру, закрыть все окна
video_capture.release()
cv2.destroyAllWindows()