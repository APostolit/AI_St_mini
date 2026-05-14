# Listing 7_1
import streamlit as st
from imageai.Classification import ImageClassification
import os

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/resnet50-19c8e357.pth'
# Путь к файлу с изображением
img_path = execution_path + '/images/image1.jpg'
prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(model_path)
# Загрузка модели
prediction.loadModel()
# Предсказание на модели
predictions, probabilities = prediction.classifyImage(img_path, result_count=3)
# Вывод результатов предсказания
col_1, col_2 = st.columns([1,3])
with col_1:
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        st.write(eachPrediction, " : ", eachProbability)
with col_2:
    st.image(img_path)