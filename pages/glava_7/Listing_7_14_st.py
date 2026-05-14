# Listing 7_14
from imageai.Classification.Custom import CustomImageClassification
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью
model_path = execution_path + '/Im_Trening/models/mobilenet_v2_epoch-14.pt'
json_path = execution_path + '/Im_Trening/models/Im_Trening_model_classes.json'
# Путь к файлу с изображением
img_path_in = execution_path + '/images/Znak3.jpg'

prediction = CustomImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(model_path)
prediction.setJsonPath(os.path.join(json_path))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(img_path_in, result_count=2)
col1, col2 = st.columns([1,4])
with col1:
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        st.write(eachPrediction , " : " , eachProbability)
with col2:
    st.image(img_path_in)