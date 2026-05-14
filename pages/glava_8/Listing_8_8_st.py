# Листинг 8_8
import os
import streamlit as st

# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_8'

# Путь к файлу с исходным изображением
st.write('Для данного модуля необходима подключенная камера.')
st.write('При работе в сети Github данный модуль заблокирован.')
st.write('Но вы можете скачать код и запустить его на своем ПК.')
img = execution_path + '/images/potok.jpg'
st.image(img)
