# Листинг 2.14
class Cat:
    Name_Class = "Кошки"
    # Свойства для объектов класса
    def __init__(self, wool_color=None, eyes_color=None, name=None):
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

my_cat = Cat()
my_cat.name = "Васька"
my_cat.wool_color = "Черный"
st.write("Наименование класса - ", my_cat.Name_Class)
st.write("Вот наша кошка:")
st.write("Цвет шерсти- ", my_cat.wool_color)
st.write("Цвет глаз- ", my_cat.eyes_color)
st.write("Кличка- ", my_cat.name)

# Апробация методов объекта
my_cat.purr()
my_cat.hiss()
my_cat.scrabble()