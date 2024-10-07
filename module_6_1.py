# Создайте 2 класса родителя: Animal, Plant
class Animal:
    def __init__(self, name):
        # Для класса Animal атрибуты alive = True (живой) и fed = False (не накормленный),
        # name - индивидуальное название каждого животного.
        self.alive = True
        self.fed = False
        self.name = name


class Plant:
    def __init__(self, name, edible=False):
        # Для класса Plant атрибут edible = False (съедобность), name - индивидуальное название каждого растения
        self.edible = edible  # По умолчанию растение несъедобное
        self.name = name


# Класс - наследник Mammal (Млекопитающие) для класса Животных.
class Mammal(Animal):
    # Метод eat для млекопитающих, позволяющий им есть растения
    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, является ли еда растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")  # Животное съело растение
                self.fed = True  # Животное накормлено
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False  # Животное погибло из-за несъедобного растения
        else:
            # Если еда не является растением
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


# Класс - наследник Predatar (Хищники) для класса Животных.
class Predator(Animal):
    # Метод eat для хищников, позволяющий им есть растения
    def eat(self, food):
        if isinstance(food, Plant):  # Проверяем, является ли еда растением
            if food.edible:  # Если растение съедобное
                print(f"{self.name} съел {food.name}")  # Хищник съел растение
                self.fed = True  # Хищник накормлен
            else:
                print(f"{self.name} не стал есть {food.name}")  # Хищник отказался от еды
                self.alive = False  # Хищник погиб из-за несъедобного растения
        else:  # Если еда не является растением
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


# Класс - наследник Flower (Цветы) для класса Растений.
class Flower(Plant):
    def __init__(self, name):
        # Вызываем конструктор родительского класса Plant и устанавливаем, что цветы несъедобные
        super().__init__(name, edible=False)


# Класс - наследник Fruit (Фрукты) для класса Растений.
class Fruit(Plant):
    def __init__(self, name):
        # Вызываем конструктор родительского класса Plant и устанавливаем, что фрукты съедобные
        super().__init__(name, edible=True)


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
