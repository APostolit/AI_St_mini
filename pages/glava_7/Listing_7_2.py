# Listing 7_2
from imageai.Classification import ImageClassification
import os

# Текущий каталог
execution_path = os.getcwd()
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
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)