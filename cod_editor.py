import streamlit as st

from code_editor import code_editor
# Дополнительные библиотеки для выполнения кода
import numpy as np
import os
import time
# import cv2
# from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
'''
import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn, optim
from torch.utils.data import DataLoader
import torch.nn.functional as F
import os
from PIL import Image
import time
import cv2

# Класс нейронной сети
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        # выход в виде вероятностей
        return F.log_softmax(x, dim=1)
'''
# Описание класса Нейрон
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    # функция активации
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return self.sigmoid(total)

def editor(path_file):
    # Загрузить код на Python_st
    file = open(path_file, 'r')
    code_st = file.read()
    # Открыть редактор кода
    with st.expander("🛠️ Редактор кода в Streamlit ✍🏻"):
        response_dict = code_editor(code_st, theme='dark')
        if len(response_dict['id']) != 0 and (
                response_dict['type'] == "selection" or response_dict['type'] == "submit"):
            code_st = response_dict.get('text')
        st.write('После редактирования для сохранения изменений нажмите CTRL+Enter')
        # Текущий каталог
        execution_path = os.getcwd()

        bt = st.button('Выполнить код', type="primary")
        if bt:
            if path_file =='pages/glava_6/Listing_6_10_st.py':
                st.write('Этот модуль требует PyTorch, карту NVIDIA 8 Гб. и 16 Гб ОЗУ.')
                with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
                    time.sleep(5)
                tab_1, tab_2, tab_3, tab_4 = st.tabs(['Обучение', 'Образцы', 'Цифры', 'Графики'])
                # Каталог главы
                execution_path = execution_path + '/pages/glava_6'
                with tab_1:
                    imd_path = execution_path + '/images/ris_6_14.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_6_15.jpg'
                    st.image(imd_path)
                with tab_3:
                    imd_path = execution_path + '/images/ris_6_16.jpg'
                    st.image(imd_path)
                with tab_4:
                    imd_path = execution_path + '/images/ris_6_17.jpg'
                    st.image(imd_path)

            elif path_file =='pages/glava_6/Listing_6_11_st.py':
                with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
                    time.sleep(10)
                    # Каталог главы
                    execution_path = execution_path + '/pages/glava_6'
                tab_1, tab_2 = st.tabs(['Точность модели', 'Потери модели'])
                with tab_1:
                    imd_path = execution_path + '/images/ris_6_29.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_6_30.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_1_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                imd_path = execution_path + '/images/ris_7_1.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_2_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                imd_path = execution_path + '/images/ris_7_2.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_3_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                imd_path = execution_path + '/images/ris_7_3.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_4_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/image5.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_7_5.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_5_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/image5.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_7_6.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_6_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/image5.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_7_7.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_7_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2, tab_3 = st.tabs(['Исходное изображение',
                                               'Обнаруженные объекты',
                                               'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/image_str.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_7_9.jpg'
                    st.image(imd_path)
                with tab_3:
                    imd_path = execution_path + '/images/image_str_out.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_8_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Исходное видео',
                                        'Обработанное видео'])
                with tab_1:
                    video_path = execution_path + '/video/transport.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")
                with tab_2:
                    video_path = execution_path + '/video/detected_h256.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")

            elif path_file == 'pages/glava_7/Listing_7_9_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Исходное видео',
                                        'Обработанное видео'])
                with tab_1:
                    video_path = execution_path + '/video/transport.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")
                with tab_2:
                    video_path = execution_path + '/video/detected_h256.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")

            elif path_file == 'pages/glava_7/Listing_7_10_st.py':
                st.write('Для данного модуля необходима подключенная камера.')
                st.write('При работе в сети Github данный модуль заблокирован.')
                st.write('Но вы можете скачать код и запустить его на своем ПК.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                imd_path = execution_path + '/images/ris_7_14.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_11_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2, tab_3 = st.tabs(['Объекты',
                                               'Исходное видео',
                                               'Обработанное видео'])
                with tab_1:
                    # Каталог главы
                    imd_path = execution_path + '/images/ris_7_16.jpg'
                    st.image(imd_path)
                with tab_2:
                    video_path = execution_path + '/video/transport.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")
                with tab_3:
                    video_path = execution_path + '/video/detected_h256.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")

            elif path_file == 'pages/glava_7/Listing_7_12_st.py':
                st.write('Данный модуль не работает на Github в среде Streamlit.')
                st.write('Но вы можете скачать код и запустить его на своем')
                st.write('компьютере в среде Python или Streamlit.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                imd_path = execution_path + '/images/ris_7_19.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_13_st.py':
                with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
                    time.sleep(10)
                st.write('Процесс обучения нейронной сети завершен')

            elif path_file == 'pages/glava_7/Listing_7_14_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_7'
                imd_path = execution_path + '/images/ris_7_26.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_15_st.py':
                with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
                    time.sleep(10)
                st.write('Процесс обучения нейронной сети завершен')

            elif path_file == 'pages/glava_7/Listing_7_16_st.py':
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Изображение 1', 'Изображение 2'])
                with tab_1:
                    imd_path = execution_path + '/images/ris_7_29.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_7_30.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_7/Listing_7_17_st.py':
                with st.spinner(text="Ждите, идет обработка видео...", show_time=True):
                    time.sleep(10)
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Исходное видео', 'Обработанное видео'])
                with tab_1:
                    video_path = execution_path + '/video/holo1.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")
                with tab_2:
                    video_path = execution_path + '/video/holo1-detected_h256.mp4'
                    video_file_in = open(video_path, "rb")
                    video_bytes_in = video_file_in.read()
                    st.video(video_bytes_in, format="video/mp4")

            elif path_file == 'pages/glava_7/Listing_7_18_st.py':
                with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
                    time.sleep(5)
                st.write('Процесс обучения нейронной сети завершен')

            elif path_file == 'pages/glava_7/Listing_7_19_st.py':
                execution_path = execution_path + '/pages/glava_7'
                tab_1, tab_2 = st.tabs(['Изображение 1', 'Изображение 2'])
                with tab_1:
                    imd_path = execution_path + '/images/ris_7_51.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_7_52.jpg'
                    st.image(imd_path)

            elif path_file == 'pages/glava_8/Listing_8_1_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/Test_Face.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/Test_Face_det.jpg'
                    st.image(imd_path)
                    
            elif path_file == 'pages/glava_8/Listing_8_2_st.py':
                st.write('Для данного модуля необходима подключенная камера.')
                st.write('При работе в сети Github данный модуль заблокирован.')
                st.write('Но вы можете скачать код и запустить его на своем ПК.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                imd_path = execution_path + '/images/ris_8_3.jpg'
                st.image(imd_path)
                
            elif path_file == 'pages/glava_8/Listing_8_3_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/Test_Face_eye.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/Test_Face_Eye_det.jpg'
                    st.image(imd_path)
                    
            elif path_file == 'pages/glava_8/Listing_8_4_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/smile.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/smile_det.jpg'
                    st.image(imd_path)
                    
            elif path_file == 'pages/glava_8/Listing_8_5_st.py':
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                tab_1, tab_2 = st.tabs(['Исходное изображение', 'Обработанное изображение'])
                with tab_1:
                    imd_path = execution_path + '/images/Test_Numer.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/Test_Numer_det.jpg'
                    st.image(imd_path)                    

            elif path_file == 'pages/glava_8/Listing_8_6_st.py':
                st.write('Для данного модуля необходима подключенная камера.')
                st.write('При работе в сети Github данный модуль заблокирован.')
                st.write('Но вы можете скачать код и запустить его на своем ПК.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                imd_path = execution_path + '/images/ris_8_11.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_8/Listing_8_7_st.py':
                st.write('Для данного модуля необходима подключенная камера.')
                st.write('При работе в сети Github данный модуль заблокирован.')
                st.write('Но вы можете скачать код и запустить его на своем ПК.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                imd_path = execution_path + '/images/ris_8_13.jpg'
                st.image(imd_path)
                
            elif path_file == 'pages/glava_8/Listing_8_9_st.py':
                execution_path = execution_path + '/pages/glava_8'
                t1, t2, t3, t4, t5, t6 = st.tabs(['Изображение', 'Все тело',
                                                  'Верх тела', 'Низ тела',
                                                  'Правый глаз', 'Левый глаз'])
                with t1:
                    imd_path = execution_path + '/images/Test4.jpg'
                    st.image(imd_path)
                with t2:
                    imd_path = execution_path + '/images/ris_8_16.jpg'
                    st.image(imd_path)
                with t3:
                    imd_path = execution_path + '/images/ris_8_17.jpg'
                    st.image(imd_path)
                with t4:
                    imd_path = execution_path + '/images/ris_8_18.jpg'
                    st.image(imd_path)
                with t5:
                    imd_path = execution_path + '/images/ris_8_19.jpg'
                    st.image(imd_path)
                with t6:
                    imd_path = execution_path + '/images/ris_8_19_1.jpg'
                    st.image(imd_path)                

            elif path_file == 'pages/glava_8/Listing_8_14_st.py':
                st.write('Для данного модуля необходима подключенная камера.')
                st.write('При работе в сети Github данный модуль заблокирован.')
                st.write('Но вы можете скачать код и запустить его на своем ПК.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                imd_path = execution_path + '/images/ris_8_34.jpg'
                st.image(imd_path)

            elif path_file == 'pages/glava_8/Listing_8_15_st.py':
                with st.spinner(text="Ждите, идет обучение модели...", show_time=True):
                    time.sleep(5)
                st.write('Процесс обучения нейронной сети завершен')

            elif path_file == 'pages/glava_8/Listing_8_16_st.py':
                st.write('Для данного модуля необходима подключенная камера.')
                st.write('При работе в сети Github данный модуль заблокирован.')
                st.write('Но вы можете скачать код и запустить его на своем ПК.')
                # Каталог главы
                execution_path = execution_path + '/pages/glava_8'
                tab_1, tab_2, tab_3, tab_4 = st.tabs(['Камера 1', 'Камера 2',
                                                      'Камера 3', 'Камера 4'])
                with tab_1:
                    imd_path = execution_path + '/images/ris_8_36.jpg'
                    st.image(imd_path)
                with tab_2:
                    imd_path = execution_path + '/images/ris_8_37.jpg'
                    st.image(imd_path)
                with tab_3:
                    imd_path = execution_path + '/images/ris_8_38.jpg'
                    st.image(imd_path)
                with tab_4:
                    imd_path = execution_path + '/images/ris_8_39.jpg'
                    st.image(imd_path)

            else:
                exec(code_st)
                '''
                    try:
                        exec(code_st)
                    except:
                        st.write('В программном коде есть ошибка!')
                '''

if __name__ == '__main__':
    path = 'pages/glava_3/Listing_3_1_st.py'
    editor(path)
