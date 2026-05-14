import streamlit as st
import cod_editor

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 4", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

# Текст по центру страницы
st.header("👩🏻‍💻Листинги главы 4")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox("Листинги главы 4",
        ("Листинг 4.1", "Листинг 4.2.1", "Листинг 4.2.2", "Листинг 4.3",
         "Листинг 4.4", "Листинг 4.5", "Листинг 4.6", "Листинг 4.7",
         "Листинг 4.8", ),
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

    elif options == "Листинг 4.1":
        path = 'pages/glava_4/Listing_4_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_4/Listing_4_1_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.2.1":
        path = 'pages/glava_4/Listing_4_2_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_4/Listing_4_2_1_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.2.2":
        path = 'pages/glava_4/Listing_4_2_2.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_4/Listing_4_2_2_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.3":
        path = 'pages/glava_4/Listing_4_3.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # with st.expander("🔍 Показать результат"):
            # fun_g4.run_4_3()
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_4/Listing_4_3_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.4":
        path = 'pages/glava_4/Listing_4_4.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        path = 'pages/glava_4/Listing_4_4_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.5":
        path = 'pages/glava_4/Listing_4_5.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        path = 'pages/glava_4/Listing_4_5_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.6":
        path = 'pages/glava_4/Listing_4_6.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        path = 'pages/glava_4/Listing_4_6_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.7":
        path = 'pages/glava_4/Listing_4_7.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        path = 'pages/glava_4/Listing_4_7_st.py'
        cod_editor.editor(path)

    elif options == "Листинг 4.8":
        path = 'pages/glava_4/Listing_4_8.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        path = 'pages/glava_4/Listing_4_8_st.py'
        cod_editor.editor(path)