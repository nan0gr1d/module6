"""
module_6_2
"""
class Vehicle():
    __COLOR_VARIANTS = ['BROWN', 'GREY', 'BLACK', 'WHITE', 'BLUE', 'YELLOW', 'RED', 'GREEN']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        """
        возвращает строку: "Модель: <название модели транспорта>"
        """
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        """
        возвращает строку: "Мощность двигателя: <мощность>"
        """
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        """
        возвращает строку: "Цвет: <цвет транспорта>"
        """
        return f"Цвет: {self.__color}"

    def print_info(self):
        """
        распечатывает результаты методов (в том же порядке):
            get_model,
            get_horsepower,
            get_color;
            "Владелец: <имя>"
        """
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        """
        меняет цвет __color на new_color,  если он есть в списке __COLOR_VARIANTS,
        в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        """
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цвета __COLOR_VARIANTS = ['BROWN', 'GREY', 'BLACK', 'WHITE', 'BLUE', 'YELLOW', 'RED', 'GREEN']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

#eof-module_6_2