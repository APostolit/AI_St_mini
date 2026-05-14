# Листинг 5.5
import numpy as np
import matplotlib.pylab as plt

class OurNeuralNetwork:
    def __init__(self):
        # Вес
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
        # Смещения
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    # Функция активации sigmoid - f(x) = 1 / (1 + e^(-x))
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Производная от sigmoid - f'(x) = f(x) * (1 - f(x))
    def deriv_sigmoid(self, x):
        fx = self.sigmoid(x)
        return fx * (1 - fx)

    # расчет среднеквадратичной ошибки
    def mse_loss(self, y_true, y_pred):
        # y_true и y_pred являются массивами numpy с одинаковой длиной
        return ((y_true - y_pred) ** 2).mean()

    def feedforward(self, x):
        # x является массивом numpy с двумя элементами
        h1 = self.sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = self.sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = self.sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    def train(self, data, all_y_trues):
        global list_epoch, list_loss
        global w1, w2, w3, w4, w5, w6, b1, b2, b3
        learn_rate = 0.1
        epochs = 1000  # количество циклов во всем наборе данных

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- Выполняем обратную связь (нам понадобятся эти значения
                #     в дальнейшем)
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = self.sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = self.sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = self.sigmoid(sum_o1)
                y_pred = o1

                # --- Подсчет частных производных
                # --- Наименование: d_L_d_w1 представляет "частично L / частично w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

                # Нейрон o1
                d_ypred_d_w5 = h1 * self.deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * self.deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = self.deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * self.deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * self.deriv_sigmoid(sum_o1)

                # Нейрон h1
                d_h1_d_w1 = x[0] * self.deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * self.deriv_sigmoid(sum_h1)
                d_h1_d_b1 = self.deriv_sigmoid(sum_h1)

                # Нейрон h2
                d_h2_d_w3 = x[0] * self.deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * self.deriv_sigmoid(sum_h2)
                d_h2_d_b2 = self.deriv_sigmoid(sum_h2)

                # --- Обновляем вес и смещения
                # Нейрон h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1
                w1 = self.w1
                w2 = self.w2
                b1 = self.b1

                # Нейрон h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2
                w3 = self.w3
                w4 = self.w4
                b2 = self.b2

                # Нейрон o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3
                w5 = self.w5
                w6 = self.w6
                b3 = self.b3

            # --- Подсчитываем общую потерю в конце каждой фазы
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = self.mse_loss(all_y_trues, y_preds)
                list_epoch.append(epoch)
                list_loss.append(loss)
                # print("Epoch %d loss: %.3f" % (epoch, loss))

# Определение набора данных
data = np.array([
    [-2, -1],  # Alice
    [25, 6],   # Bob
    [17, 4],   # Charlie
    [-15, -6], # Diana
])

all_y_trues = np.array([
    1,  # Alice
    0,  # Bob
    0,  # Charlie
    1,  # Diana
])

# Список для хранения эпох
list_epoch = []
# Список для хранения ошибок обучения
list_loss = []
# Объекты для хранения параметров обучения
w1=w2=w3=w4=w5=w6=b1=b2=b3 = None

# Тренируем нашу нейронную сеть!
network = OurNeuralNetwork()
network.train(data, all_y_trues)

# Рисуем график
plt.xlabel('Эпохи обучения') # подпись оси х
plt.ylabel('Потери (ошибки)')  # подпись оси y
# Построение графика
plt.plot(list_epoch, list_loss)
# Отображение графика
plt.show()

# Задаем параметры людей для теста
men_1 = np.array([-7, -3])  # 128 фунтов, 63 дюйма
men_2 = np.array([20, 2])   # 155 фунтов, 68 дюймов
print('Параметры людей для теста сети')
print('men_1=', men_1, ' men_2=', men_2)

# Делаем предсказания
p_men_1 = network.feedforward(men_1)
p_men_2 = network.feedforward(men_2)

print('Результаты предсказания')
print("men_1: %.3f" % p_men_1)
print("men_2: %.3f" % p_men_2)

print('Итог тестирования сети')
if p_men_1>= 0.5:
    print('men_1- женщина')
else:
    print('men_1 - мужчина')

if p_men_2 >= 0.5:
    print('men_2 - женщина')
else:
    print('men_2 - мужчина')

print('Параметры сети после обучения')
print('w1=', w1, 'w2=', w2, 'b1=', b1)
print('w3=', w3, 'w4=', w4, 'b2=', b2)
print('w5=', w5,'w6=', w6, 'b3=', b3)