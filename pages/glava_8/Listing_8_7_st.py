# Листинг 8_7
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'

# Путь к файлу с исходным изображением
img_path_znak = execution_path + '/images/znak.jpg'
# Путь к файлу с обработанным изображением
img_path_avto_znak = execution_path + '/images/avto_znak.jpg'

col1, col2 = st.columns([3, 1])

with col1:
    st.image(img_path_avto_znak)
with col2:
    st.image(img_path_znak)
