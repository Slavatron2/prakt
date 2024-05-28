#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
#шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
#"кличка" и "порода".
class Animal:
    def __init__(self, species, num_legs, fur_color):
        self.species = species
        self.num_legs = num_legs
        self.fur_color = fur_color

    def describe(self):
        print(f"Это {self.species} с {self.num_legs} лапами и c {self.fur_color} окрасом.")

class Dog(Animal):
    def __init__(self, species, num_legs, fur_color, name, breed):
        super().__init__(species, num_legs, fur_color)
        self.name = name
        self.breed = breed

    def describe(self):
        super().describe()
        print(f"{self.name} - это {self.breed}.")

dog = Dog("Собака", 4, "коричневый", "Дружок", "Лабрадор")
dog.describe()
