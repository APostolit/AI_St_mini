# Listing 7_2
from imageai.Classification import ImageClassification
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/inception_v3_google-1a9a5a14.pth'
# Путь к файлу с изображением
img_path = execution_path + '/images/image4.jpg'

prediction = ImageClassification()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(execution_path, model_path))
# Загрузка модели
prediction.loadModel()

# Предсказание на модели
predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, img_path), result_count=3)
# Вывод результатов предсказания
col_1, col_2 = st.columns([1,3])
with col_1:
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        st.write(eachPrediction, " : ", eachProbability)
with col_2:
    st.image(img_path)
