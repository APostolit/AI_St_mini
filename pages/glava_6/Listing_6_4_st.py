# Листинг 6.4
from sklearn.datasets import load_iris
import streamlit as st

# Загрузка набора данных из библиотеки sklearn
# Вывод характеристик набора данных
iris_dataset = load_iris()
st.write("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))
st.write("Тип массива данных: {}".format(type(iris_dataset['data'])))
st.write("Форма массива данных: {}".format(iris_dataset['data'].shape))
st.write("Классификационные признаки (цель): {}".format(iris_dataset['target']))
st.write("Названия ответов: {}".format(iris_dataset['target_names']))
st.write('Описание набора данных ----------------------------------')
st.write(iris_dataset['DESCR'][:193] + "\n...")
st.write('----------------------------------------------------------')
st.write("Названия признаков: \n{}".format(iris_dataset['feature_names']))
st.write("Название файла файла: \n{}".format(iris_dataset['filename']))