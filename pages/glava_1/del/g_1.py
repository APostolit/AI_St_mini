import streamlit as st
import cod_editor

# Настройка параметров данной страницы
st.set_page_config(
    page_title="Глава 1", # Текст на вкладке браузера
    page_icon='📕',       # Иконка на вкладке браузера
    layout="wide",        # Использовать всю ширину страницы
    initial_sidebar_state="collapsed",  # Развернуть боковую панель
)

st.header("👩🏻‍💻Листинги главы 1")

# Боковая панель
with st.sidebar:
    # Контейнер
    cont_1 = st.container(width=300)

with cont_1:
    # Раскрывающийся список
    options = st.selectbox(
        "Листинги главы 1",
        ("Листинг 1.1", ),
        index=None,
        placeholder="Выберите листинг..."
    )

# Контейнер
cont = st.container(width=800)

with cont:
    if options is None:
        st.write('Листинг не выбран')
        st.image("Python_Book.jpg", width=350)

    elif options == "Листинг 1.1":
        path = 'pages/glava_1/Listing_1_1.py'
        file = open(path, 'r')
        code = file.read()
        st.code(code, language="python", line_numbers=True)
        # Загрузить и редактировать код на Python_st
        path = 'pages/glava_1/Listing_1_1_st.py'
        cod_editor.editor(path)
