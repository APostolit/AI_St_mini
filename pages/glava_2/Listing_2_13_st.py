# Листинг 2.13
class Cat:
    Name_Class = "Кошки"
    # Свойства для объектов класса
    def __init__(self, wool_color, eyes_color, name):
        self.wool_color = wool_color
        self.eyes_color = eyes_color
        self.name = name

    # Мурлыкать (метод)
    def purr(self):
        st.write("Муррр!")

    # Шипеть (метод)
    def hiss(self):
        st.write("Шшшш!")

    # Царапаться (метод)
    def scrabble(self):
        st.write("Цап-царап!")

my_cat = Cat('Белая', 'Зеленые', 'Мурка')
st.write("Наименование класса - ", my_cat.Name_Class)
st.write("Вот наша кошка:")
st.write("Цвет шерсти- ", my_cat.wool_color)
st.write("Цвет глаз- ", my_cat.eyes_color)
st.write("Кличка- ", my_cat.name)