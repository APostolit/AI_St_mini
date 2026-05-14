# Листинг 6.3
import pandas as pd
import streamlit as st

data = {'Имя': ["Дима", "Анна", "Петр", "Вика"],
        'Город': ["Москва", "Курск", "Псков", "Воронеж"],
        'Возраст': [24, 13, 53, 33]}
with st.container(width=300):
    df = pd.DataFrame(data)
    st.dataframe(df)