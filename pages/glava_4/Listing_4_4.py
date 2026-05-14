# Листинг 4.4
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

print('Весовые коэффициенты после обучения нейрона')
print(weights)  # Вывод значений весов

# проверка работы программы на обучающей выборке
print("0 это 5? ", perceptron(num0))
print("1 это 5? ", perceptron(num1))
print("2 это 5? ", perceptron(num2))
print("3 это 5? ", perceptron(num3))
print("4 это 5? ", perceptron(num4))
print("5 это 5? ", perceptron(num5))
print("6 это 5? ", perceptron(num6))
print("7 это 5? ", perceptron(num7))
print("8 это 5? ", perceptron(num8))
print("9 это 5? ", perceptron(num9))