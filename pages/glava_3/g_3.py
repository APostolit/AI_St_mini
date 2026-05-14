import streamlit as st
import cod_editor

import subprocess
import sys

from code_editor import code_editor
from  streamlit_execute  import  init
import streamlit_execute as se

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 3", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 3")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 3",
        ("Листинг 3.1", "Листинг 3.2", "Листинг 3.3", "Листинг 3.4", "Листинг 3.5"),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    # st.page_link('https://pythonlib.ru/sandbox', label='🛠️ Редактор код ✍🏻')
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 3.1":
        # Загрузить и показать код на Python
        path = 'pages/glava_3/Listing_3_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_3/Listing_3_1_st.py'
        cod_editor.editor(path)


    elif options == "Листинг 3.2":
        path = 'pages/glava_3/Listing_3_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_3/Listing_3_2_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 3.3":
        path = 'pages/glava_3/Listing_3_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_3/Listing_3_3_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 3.4":
        path = 'pages/glava_3/Listing_3_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_3/Listing_3_4_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 3.5":
        path = 'pages/glava_3/Listing_3_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_3/Listing_3_5_st.py'
        cod_editor.editor(path)
