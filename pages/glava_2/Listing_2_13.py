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
        print("Муррр!")

    # Шипеть (метод)
    def hiss(self):
        print("Шшшш!")

    # Царапаться (метод)
    def scrabble(self):
        print("Цап-царап!")

my_cat = Cat('Белая', 'Зеленые', 'Мурка')
print("Наименование класса - ", my_cat.Name_Class)
print("Вот наша кошка:")
print("Цвет шерсти- ", my_cat.wool_color)
print("Цвет глаз- ", my_cat.eyes_color)
print("Кличка- ", my_cat.name)