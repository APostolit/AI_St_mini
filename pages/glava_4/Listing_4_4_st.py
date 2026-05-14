import streamlit as st
import random

# Обучающая выборка (идеальное изображение цифр от 0 до 9)
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
# Список всех цифр от 0 до 9 в едином массиве
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

tema = 5                                # какой цифре обучаем
n_sensor = 15                           # количество сенсоров
weights = [0 for i in range(n_sensor)]  # обнуление весов

# Функция определяет, является ли полученное изображение числом 5
# Возвращает Да, если признано, что это 5. Возвращает Нет, если отвергнуто, что это 5
def perceptron(Sensor):
    global weights, n_sensor
    b = 7  # Порог функции активации
    s = 0  # Начальное значение суммы
    for i in range(n_sensor):  # цикл суммирования сигналов от сенсоров
        s += int(Sensor[i]) * weights[i]
    # print(weights)
    if s >= b:
        return True   # Сумма превысила порог
    else:
        return False  # Сумма меньше порога

# Уменьшение значений весов
# Если сеть ошиблась и выдала Да при входной цифре, отличной от пятерки
def decrease(number):
    global weights, n_sensor
    for i in range(n_sensor):
        if int(number[i]) == 1:  # Если вход возбужден
            weights[i] -= 1      # Уменьшаем связанный с входом вес на единицу

# Увеличение значений весов
# Если сеть ошиблась и выдала Нет при поданной на вход цифре 5
def increase(number):
    global weights, n_sensor
    for i in range(n_sensor):
        if int(number[i]) == 1:  # Если вход возбужден
            weights[i] += 1      # Увеличиваем связанный с входом вес на единицу

# Тренировка сети
n = 1000  # количество уроков
for k in range(n):
    j = random.randint(0, 9)  # Генерируем случайное число j от 0 до 9
    # j = 5
    r = perceptron(nums[j])   # Результат обращения к сумматору
                              # (ответ - Да или НЕТ)

    if j != tema:  # Если генератор выдал случайное число j не равное 5
        if r:  # Если сумматор сказал True (ДА)- это пятерка,
               # а j - это не пятерка
            decrease(nums[j])  # Ошибка первого типа,
                               #уменьшаем значимые веса

    else:  # Если генератор выдал случайное число j равное 5
        if not r:  # Если сумматор сказал False (НЕТ)- это не пятерка,
                   # а на самом деле j=5
            increase(nums[tema])  # Ошибка второго типа,
                                  #увеличиваем значимые веса

st.text('Весовые коэффициенты после обучения нейрона')
st.text(weights)  # Вывод значений весов
w = weights

col_1, col_2 = st.columns(2)
with col_1:
    # проверка работы программы на обучающей выборке
    st.write("0 это 5? ", perceptron(num0))
    st.write("1 это 5? ", perceptron(num1))
    st.write("2 это 5? ", perceptron(num2))
    st.write("3 это 5? ", perceptron(num3))
    st.write("4 это 5? ", perceptron(num4))
    st.write("5 это 5? ", perceptron(num5))
    st.write("6 это 5? ", perceptron(num6))
    st.write("7 это 5? ", perceptron(num7))
    st.write("8 это 5? ", perceptron(num8))
    st.write("9 это 5? ", perceptron(num9))

with col_2:
    st.write('Вид распознанной цифры', tema)
    col1, col2, col3 = st.columns(3, width=100)
    with col1:
        if w[0] >= 1:
            st.write('📕')
    with col2:
        if w[1] >= 1:
            st.write('📕')
    with col3:
        if w[2] >= 1:
            st.write('📕')

    col1, col2, col3 = st.columns(3, width=100)
    with col1:
        if w[3] >= 1:
            st.write('📕')
    with col2:
        if w[4] >= 1:
            st.write('📕')
    with col3:
        if w[5] >= 1:
            st.write('📕')

    col1, col2, col3 = st.columns(3, width=100)
    with col1:
        if w[6] >= 1:
            st.write('📕')
    with col2:
        if w[7] >= 1:
            st.write('📕')
    with col3:
        if w[8] >= 1:
            st.write('📕')

    col1, col2, col3 = st.columns(3, width=100)
    with col1:
        if w[9] >= 1:
            st.write('📕')
    with col2:
        if w[10] >= 1:
            st.write('📕')
    with col3:
        if w[11] >= 1:
            st.write('📕')

    col1, col2, col3 = st.columns(3, width=100)
    with col1:
        if w[12] >= 1:
            st.write('📕')
    with col2:
        if w[13] >= 1:
            st.write('📕')
    with col3:
        if w[14] >= 1:
            st.write('📕')