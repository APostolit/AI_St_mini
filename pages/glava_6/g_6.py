import streamlit as st
import cod_editor

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 6", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 6")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 6",
        ("Листинг 6.1", "Листинг 6.2", "Листинг 6.3", "Листинг 6.4",
         "Листинг 6.5", "Листинг 6.6", "Листинг 6.7", "Листинг 6.8",
         "Листинг 6.9", "Листинг 6.10", "Листинг 6.11", "Листинг 6.12",
         "Листинг 6.13", "Листинг 6.14"
         ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont_2 = st.container(width=800)
with cont_2:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 6.1":
        path = 'pages/glava_6/Listing_6_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_1_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.2":
        path = 'pages/glava_6/Listing_6_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_2_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.3":
        path = 'pages/glava_6/Listing_6_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_3_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.4":
        path = 'pages/glava_6/Listing_6_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_4_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.5":
        path = 'pages/glava_6/Listing_6_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_5_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.6":
        path = 'pages/glava_6/Listing_6_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_6_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.7":
        path = 'pages/glava_6/Listing_6_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_7_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.8":
        path = 'pages/glava_6/Listing_6_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_8_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.9":
        path = 'pages/glava_6/Listing_6_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_9_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.10":
        path = 'pages/glava_6/Listing_6_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_10_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.11":
        path = 'pages/glava_6/Listing_6_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_11_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.12":
        path = 'pages/glava_6/Listing_6_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_12_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.13":
        path = 'pages/glava_6/Listing_6_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_13_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 6.14":
        path = 'pages/glava_6/Listing_6_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_6/Listing_6_14_st.py'
        cod_editor.editor(path)