# https://python-code-online.pages.dev/ru/
import streamlit as st
import cod_editor

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 2", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="auto",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 2")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

# Контейнер
with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 2",
        ("Листинг 2.1", "Листинг 2.2", "Листинг 2.3", "Листинг 2.4",
         "Листинг 2.5", "Листинг 2.6", "Листинг 2.7", "Листинг 2.8",
         "Листинг 2.9", "Листинг 2.10", "Листинг 2.11", "Листинг 2.12",
         "Листинг 2.13", "Листинг 2.14", "Листинг 2.15",
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

    elif options == "Листинг 2.1":
        # Загрузить и показать код на Python
        path = 'pages/glava_2/Listing_2_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_1_st.py'
        cod_editor.editor(path)


    elif options == "Листинг 2.2":
            # Загрузить и показать код на Python
        path = 'pages/glava_2/Listing_2_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_2_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.3":
            # Загрузить и показать код на Python
        path = 'pages/glava_2/Listing_2_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_3_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.4":
            # Загрузить и показать код на Python
        path = 'pages/glava_2/Listing_2_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_4_st.py'
        cod_editor.editor(path)


    elif options == "Листинг 2.5":
            # Загрузить и показать код на Python
        path = 'pages/glava_2/Listing_2_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_5_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.6":
            # Загрузить и показать код на Python
        path = 'pages/glava_2/Listing_2_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_6_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.7":
        path = 'pages/glava_2/Listing_2_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_7_st.py'
        cod_editor.editor(path)


    elif options == "Листинг 2.8":
        path = 'pages/glava_2/Listing_2_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_8_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.9":
        path = 'pages/glava_2/Listing_2_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_9_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.10":
        path = 'pages/glava_2/Listing_2_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_10_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.11":
        path = 'pages/glava_2/Listing_2_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_11_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.12":
        path = 'pages/glava_2/Listing_2_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_12_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.13":
        path = 'pages/glava_2/Listing_2_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_13_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.14":
        path = 'pages/glava_2/Listing_2_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_14_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 2.15":
        path = 'pages/glava_2/Listing_2_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
            # Загрузить и редактировать код на Python_st
        path = 'pages/glava_2/Listing_2_15_st.py'
        cod_editor.editor(path)