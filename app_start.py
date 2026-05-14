#  pip install -r requirements.txt
import streamlit as st

# Сделать доступной всю ширину страницы
st.set_page_config(layout="wide")
st.set_page_config(initial_sidebar_state="collapsed")

# Иконка приложения
with st.sidebar:
    st.logo(image='favicon.ico', icon_image='favicon.ico', size="large")

# Глава 1
g_1 = st.Page(page="pages/glava_1/g_1.py", title="📕Листинги главы 1")
# Глава 2
g_2 = st.Page(page="pages/glava_2/g_2.py", title="📕Листинги главы 2")
# Глава 3
g_3 = st.Page(page="pages/glava_3/g_3.py", title="📕Листинги Главы 3")
# Глава 4
g_4 = st.Page(page="pages/glava_4/g_4.py", title="📕Листинги Главы 4")

# Глава 5
g_5 = st.Page(page="pages/glava_5/g_5.py", title="📕Листинги главы 5")

# Глава 6
g_6 = st.Page(page="pages/glava_6/g_6.py", title="📕Листинги главы 6")

# Глава 7
g_7 = st.Page(page="pages/glava_7/g_7.py", title="📕Листинги главы 7")

# Глава 8
g_8 = st.Page(page="pages/glava_8/g_8.py", title="📕Листинги главы 8")

# Создание навигатора страниц (главное меню)
pages = {
    "Глава 1": [g_1],
    "Глава 2": [g_2],
    "Глава 3": [g_3],
    "Глава 4": [g_4],
    "Глава 5": [g_5],
    "Глава 6": [g_6],
    "Глава 7": [g_7],
    "Глава 8": [g_8],
    }
pg = st.navigation(pages=pages, position="top", expanded=False)

# Запуск навигатора страниц
pg.run()

# streamlit run app_start.py
# pip freeze > requirements.txt
# pip install -r requirements.txt
