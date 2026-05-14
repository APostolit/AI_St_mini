# Listing 7_3
from imageai.Classification import ImageClassification
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + '/models/densenet121-a639ec97.pth'

prediction = ImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path, model_path))
# Загрузка модели
prediction.loadModel()

# массив с файлами рисунков
all_images_array = []
# Папка с рисунками
path_images = execution_path + '/images2/'
files = os.listdir(path_images)

# Выборка рисунков из заданной папки
for each_file in files:
   all_images_array.append(path_images + each_file)

# Цикл обработки рисунков
for img_path in  all_images_array:
    col_1, col_2 = st.columns([1, 3])
    with col_1:
        # Предсказания
        predictions, probabilities = prediction.classifyImage(
            os.path.join(execution_path, img_path), result_count=3)
        # Вывод результатов предсказания
        for eachPrediction, eachProbability in zip(predictions, probabilities):
            st.write(eachPrediction, " : ", eachProbability)
        st.write('------------------------')
    with col_2:
        st.image(img_path)