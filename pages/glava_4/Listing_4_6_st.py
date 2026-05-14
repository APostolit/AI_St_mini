# Листинг 4.6
import streamlit as st
import random
import pandas as pd
import plotly.graph_objs as go

# Случайные значения параметров для начальной прямой
k = random.uniform(-3, 3)  # Коэффициент при x
c = random.uniform(-3, 3)  # Свободный член уравнения прямой
st.write('Начальная прямая: Y =  ', k, '* X + ', c)  # Вывод данных начальной прямой

# Данные для построения графика начальной прямой
x_data = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
y_data = [k * x + c for x in x_data]
# st.text(y_data)

# Набор данных для графика точек
data_g = {'x': [22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
          'y': [150, 155, 160, 162, 171, 174, 180, 183, 189, 193],}
# Преобразуем словарь в DataFrame
df = pd.DataFrame(data_g)

# Набор точек X:Y (размер обуви, рост)
data = {22: 150, 23: 155, 24: 160, 25: 162, 26: 171,
        27: 174, 28: 180, 29: 183, 30: 189, 31: 192}

# Расчет параметра Y
def proceed(x):
    global k, c
    return x * k + c

rate = 0.0001  # Шаг изменения параметров
n = 1000       # Количество циклов обучения
# Тренировка сети
for i in range(n):
    x = random.choice(list(data.keys()))  # Получить случайную X-координату точки
    true_result = data[x]      # Получить соответствующую Y-координату точки
    out = proceed(x)           # Получить ответ сети
    delta = true_result - out  # Считаем ошибку сети
    k += delta * rate * x      # Меняем вес "k" при x в соответствии с дельта-правилом
    c += delta * rate          # Меняем вес "c" в соответствии с дельта-правилом

st.write('Прямая аппроксимации: Y = ', k, '* X + ', c)  # Вывод данных готовой прямой
# Данные для оси y найденной прямой
y_new = [k * x + c for x in x_data]

# Создание макета графика
fig = go.Figure()
# Добавление к макету данных исходной линии
fig.add_trace(go.Scatter(x=x_data, y=y_data,
                         mode='lines+markers',
                         name='Случайная линия'))
# Добавление к макету данных экспериментальных точек
fig.add_trace(go.Scatter(x=df['x'], y=df['y'],
                         mode='markers',
                         name='Значения роста'
                         ))
# Добавление к макету данных линии аппроксимации
fig.add_trace(go.Scatter(x=x_data, y=y_new,
                         mode='lines',
                         name='Найденная линия'
                         ))
# Добавление параметров к макету
fig.update_layout(xaxis=dict(title='Размер обуви'),
                  yaxis=dict(title='Рост'),
                  title='Линейная аппроксимация с использованием дельта правила',
                  paper_bgcolor='lightgray',
                 )
st.plotly_chart(fig, theme=None)