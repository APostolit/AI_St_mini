# Listing 7_18
from imageai.Detection.Custom import DetectionModelTrainer
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + "/models/yolov3.pt"
# Путь к обучающей выборке
data_set = execution_path + "/Im_Yolo_Trening/"
# Создание модели
trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory=data_set)
trainer.setTrainConfig(object_names_array=["zebra", "stop"],
                       batch_size=4,
                       num_experiments=50,
                       train_from_pretrained_model=model_path
                       )
# Обучение
with st.spinner(text="Ждите, идет процесс обучения...", show_time=True):
    trainer.trainModel()
st.write('Процесс обучения нейронной сети завершен')