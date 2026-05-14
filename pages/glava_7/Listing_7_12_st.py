# Listing 7_12
from imageai.Detection import VideoObjectDetection
import os
from matplotlib import pyplot as plt
import streamlit as st

color_index = {'bus': 'red', 'handbag': 'steelblue', 'giraffe': 'orange',
               'spoon': 'gray', 'cup': 'yellow', 'chair': 'green',
               'elephant': 'pink', 'truck': 'indigo',
               'motorcycle': 'azure','refrigerator': 'gold',
               'keyboard': 'violet', 'cow': 'magenta',
               'mouse': 'crimson', 'sports ball': 'raspberry',
               'horse': 'maroon', 'cat': 'orchid', 'boat': 'slateblue',
               'hot dog': 'navy', 'apple': 'cobalt',
               'parking meter': 'aliceblue', 'sandwich': 'skyblue',
               'skis': 'deepskyblue', 'microwave': 'peacock',
               'knife': 'cadetblue', 'baseball bat': 'cyan',
               'oven': 'lightcyan', 'carrot': 'coldgrey',
               'scissors': 'seagreen', 'sheep': 'deepgreen',
               'toothbrush': 'cobaltgreen', 'fire hydrant': 'limegreen',
               'remote': 'forestgreen', 'bicycle': 'olivedrab',
               'toilet': 'ivory', 'tv': 'khaki', 'skateboard':
               'palegoldenrod', 'train': 'cornsilk', 'zebra': 'wheat',
               'tie': 'burlywood', 'orange': 'melon', 'bird': 'bisque',
               'dining table': 'chocolate','hair drier': 'sandybrown',
               'cell phone': 'sienna', 'sink': 'coral', 'bench':
               'salmon', 'bottle': 'brown', 'car': 'silver', 'bowl':
               'maroon', 'tennis racket': 'palevilotered', 'airplane':
               'lavenderblush', 'pizza': 'hotpink', 'umbrella':
               'deeppink', 'bear': 'plum', 'fork': 'purple', 'laptop':
               'indigo', 'vase': 'mediumpurple', 'baseball glove':
               'slateblue', 'traffic light': 'mediumblue','bed': 'navy',
               'broccoli': 'royalblue', 'backpack': 'slategray',
               'snowboard': 'skyblue', 'kite': 'cadetblue', 'teddy bear':
               'peacock', 'clock': 'lightcyan', 'wine glass': 'teal',
               'frisbee': 'aquamarine', 'donut': 'mincream', 'suitcase':
               'seagreen', 'dog': 'springgreen', 'banana':
               'emeraldgreen', 'person': 'honeydew','surfboard':
               'palegreen', 'cake': 'sapgreen', 'book': 'lawngreen',
               'potted plant': 'greenyellow', 'toaster': 'ivory',
               'stop sign': 'beige', 'couch': 'khaki'}

resized = False
# Текущий каталог
execution_path = os.getcwd()
execution_path = execution_path + '/pages/glava_7'

# Путь к файлу с моделью сети
model_path = execution_path + "/models/yolov3.pt"
# Путь к файлам с видео
video_path_in = execution_path + "/video/transport.mp4"
video_path_out = execution_path + "/video/video_frame_analys.mp4"
st.write(video_path_in)
st.write(video_path_out)

video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(model_path)
video_detector.loadModel()

def detect_frame(frame_number, output_array, output_count, returned_frame):
    global resized, video_path_in, video_path_out, color_index
    plt.clf()
    this_colors = []
    labels = []
    sizes = []
    counter = 0
    st.write('Попал в функцию ++++++++++++++++++++++++++++++++++++++++++++++++')
    st.write(returned_frame)

    for eachItem in output_count:
        counter += 1
        labels.append(eachItem + " = " + str(output_count[eachItem]))
        sizes.append(output_count[eachItem])
        this_colors.append(color_index[eachItem])

    if (resized == False):
        manager = plt.get_current_fig_manager()
        manager.resize(width=1000, height=500)
        resized = True

    plt.subplot(1, 2, 1)
    plt.title("Frame : " + str(frame_number))
    plt.axis("off")
    plt.imshow(returned_frame, interpolation="none")

    plt.subplot(1, 2, 2)
    plt.title("Analysis: " + str(frame_number))
    plt.pie(sizes, labels=labels, colors=this_colors,
            shadow=True, startangle=140, autopct="%1.1f%%")
    plt.pause(0.01)


# st.video(video_path_in)
# st.video(video_path_out)


# st.pyplot(plt)
# plt.show()

# with st.spinner(text="Ждите, идет обработка видео...", show_time=True):
st.write('Перед входом в функцию -------------------------------------------------')
video_detector.detectObjectsFromVideo(
    input_file_path=video_path_in,
    # output_file_path=video_path_out,
    save_detected_video=False,
    frames_per_second=20,
    per_frame_function=detect_frame,
    minimum_percentage_probability=30,
    return_detected_frame=False)
