import streamlit as st
import cod_editor

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 8", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 8")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 8",
        ("Листинг 8.1", "Листинг 8.2", "Листинг 8.3", "Листинг 8.4",
         "Листинг 8.5", "Листинг 8.6", "Листинг 8.7", "Листинг 8.8",
         "Листинг 8.9", "Листинг 8.10", "Листинг 8.11", "Листинг 8.12",
         "Листинг 8.13", "Листинг 8.14", "Листинг 8.15", "Листинг 8.16",
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

    elif options == "Листинг 8.1":
        path = 'pages/glava_8/Listing_8_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_1_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.2":
        path = 'pages/glava_8/Listing_8_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_2_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.3":
        path = 'pages/glava_8/Listing_8_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_3_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.4":
        path = 'pages/glava_8/Listing_8_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_4_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.5":
        path = 'pages/glava_8/Listing_8_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_5_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.6":
        path = 'pages/glava_8/Listing_8_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_6_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.7":
        path = 'pages/glava_8/Listing_8_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_7_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.8":
        path = 'pages/glava_8/Listing_8_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_8_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.9":
        path = 'pages/glava_8/Listing_8_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_9_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.10":
        path = 'pages/glava_8/Listing_8_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_10_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.11":
        path = 'pages/glava_8/Listing_8_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_11_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.12":
        path = 'pages/glava_8/Listing_8_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_12_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.13":
        path = 'pages/glava_8/Listing_8_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_13_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.14":
        path = 'pages/glava_8/Listing_8_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_14_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.15":
        path = 'pages/glava_8/Listing_8_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_15_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 8.16":
        path = 'pages/glava_8/Listing_8_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_8/Listing_8_16_st.py'
        cod_editor.editor(path)

