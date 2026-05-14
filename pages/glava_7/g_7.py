import streamlit as st
import cod_editor

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 7", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 7")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 7",
        ("Листинг 7.1", "Листинг 7.2", "Листинг 7.3", "Листинг 7.4",
         "Листинг 7.5", "Листинг 7.6", "Листинг 7.7", "Листинг 7.8",
         "Листинг 7.9", "Листинг 7.10", "Листинг 7.11", "Листинг 7.12",
         "Листинг 7.13", "Листинг 7.14", "Листинг 7.15", "Листинг 7.16",
         "Листинг 7.17", "Листинг 7.18", "Листинг 7.19"
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

    elif options == "Листинг 7.1":
        path = 'pages/glava_7/Listing_7_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_1_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.2":
        path = 'pages/glava_7/Listing_7_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_2_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.3":
        path = 'pages/glava_7/Listing_7_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_3_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.4":
        path = 'pages/glava_7/Listing_7_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_4_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.5":
        path = 'pages/glava_7/Listing_7_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_5_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.6":
        path = 'pages/glava_7/Listing_7_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_6_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.7":
        path = 'pages/glava_7/Listing_7_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_7_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.8":
        path = 'pages/glava_7/Listing_7_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_8_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.9":
        path = 'pages/glava_7/Listing_7_9.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_9_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.10":
        path = 'pages/glava_7/Listing_7_10.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_10_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.11":
        path = 'pages/glava_7/Listing_7_11.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_11_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.12":
        path = 'pages/glava_7/Listing_7_12.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_12_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.13":
        path = 'pages/glava_7/Listing_7_13.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_13_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.14":
        path = 'pages/glava_7/Listing_7_14.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_14_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.15":
        path = 'pages/glava_7/Listing_7_15.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_15_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.16":
        path = 'pages/glava_7/Listing_7_16.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_16_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.17":
        path = 'pages/glava_7/Listing_7_17.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_17_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.18":
        path = 'pages/glava_7/Listing_7_18.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_18_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 7.19":
        path = 'pages/glava_7/Listing_7_19.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_7/Listing_7_19_st.py'
        cod_editor.editor(path)