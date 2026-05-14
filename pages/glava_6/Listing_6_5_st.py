import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.datasets import load_iris
import streamlit as st

# Загрузить набор данных
iris_dataset = load_iris()

# Построить матрицу рассеяния с библиотекой seaborn
df = sb.load_dataset('iris')
sb.set_style("ticks")
sb.pairplot(df, hue='species', diag_kind="kde", kind="scatter", palette="husl")
st.pyplot(plt)