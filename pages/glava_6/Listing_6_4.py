# Листинг 6.4
from sklearn.datasets import load_iris

# Загрузка набора данных из библиотеки sklearn
# Вывод характеристик набора данных
iris_dataset = load_iris()
print("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))
print("Тип массива данных: {}".format(type(iris_dataset['data'])))
print("Форма массива данных: {}".format(iris_dataset['data'].shape))
print("Классификационные признаки (цель): {}".format(iris_dataset['target']))
print("Названия ответов: {}".format(iris_dataset['target_names']))
print('Описание набора данных ----------------------------------')
print(iris_dataset['DESCR'][:193] + "\n...")
print('----------------------------------------------------------')
print("Названия признаков: \n{}".format(iris_dataset['feature_names']))
print("Название файла файла: \n{}".format(iris_dataset['filename']))
