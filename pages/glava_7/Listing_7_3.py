# Listing 7_3
from imageai.Classification import ImageClassification
import os

# Текущий каталог
execution_path = os.getcwd()
# Путь к файлу с моделью сети
model_path = execution_path + '/models/densenet121-a639ec97.pth'

prediction = ImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path, model_path))
# Загрузка модели
prediction.loadModel()

# Массив с файлами рисунков
all_images_array = []
# Папка с рисунками
all_files = os.listdir('images2/')
# Выборка рисунков из заданной папки
for each_file in all_files:
    if each_file.endswith(".jpg") or each_file.endswith(".png"):
        all_images_array.append(execution_path + "/images2/" + each_file)

# Цикл обработки рисунков
for img_path in all_images_array:
    # Предсказания
    predictions, probabilities = prediction.classifyImage(
        os.path.join(execution_path, img_path), result_count=3)
    # Вывод результатов предсказания
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(eachPrediction, " : ", eachProbability)
    print('------------------------')