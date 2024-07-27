"""
module_6_1
"""
class Plant:
    #name = ''       # индивидуальное название каждого растения
    edible = False  # (съедобность)

    def __init__(self, name):
        self.name = name

class Animal:
    #name = ''     # индивидуальное название каждого животного
    alive = True  # (живой)
    fed = False   # (накормленный)

    def __init__(self, name):
        self.name = name

    def eat(self, food: Plant):
        """
        Метод eat должен работать следующим образом:
        Если переданное растение (food) съедобное - выводит на экран
        "<self.name> съел <food.name>",
        меняется атрибут fed на True.
        Если переданное растение (food) не съедобное - выводит на экран
        "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
        Т.е если животному дать съедобное растение, то животное насытится,
        если не съедобное - погибнет.
        """
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True

"""
Пункты задачи:
Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами. 
При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.
"""

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

#eof-module_6_1.py