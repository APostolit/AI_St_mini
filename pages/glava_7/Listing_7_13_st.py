# Listing 7_13
from imageai.Classification.Custom import ClassificationModelTrainer
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'
# Путь к обучающей выборке
data_set = execution_path + "/Im_Trening/"

model_trainer = ClassificationModelTrainer()
model_trainer.setModelTypeAsMobileNetV2()
model_trainer.setDataDirectory(data_set)
with st.spinner(text="Ждите, идет процесс обучения...", show_time=True):
    model_trainer.trainModel(num_experiments=20)
st.write('Процесс обучения нейронной сети завершен')