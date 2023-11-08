#1 задание
class Auto:
    def __init__(self, brand: str, age: int, mark: str, weight, color):
      self.brand = brand
      self.age = age
      self.mark = mark
      self.weight = weight
      self.color = color

    def move(self) -> None:
        print(f"move")

    def stop(self) -> None:
        print (f"stop")

    def birthday(self) -> int:
        return self.age + 1

a = Auto("Audi", 5, "A6", 128, "Black")

print(a.birthday())

#2 задание - тут что-то не так со строкой, где определяется метод move

class Truck(Auto):
   def __init__(self, brand: str, age: int, mark: str, weight, color, max_load: int, *args, **kwargs):
       super().__init__(self, brand, age, mark, weight, color, *args, **kwargs)
       self.max_load = max_load

    def move(self) -> None:
        print("Attention!")
        super().move()

import time

   def load(self) -> None:
       time.sleep(1)
       print("load")
       time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, weight, color, max_speed: int):
        self.max_speed = max_speed
    def move(self) -> None:
        print(f"move", "max_speed is", {self.max_speed})

b = Truck("audi", 12, "a6", 125)
print(b.move())
print(b.load())

c = Truck("Opel", 5, "Asstra", 295)
print(c.move())
print(c.load())

d = Car("BMW", 250,  "3", 5, "green", 250)
print(d.move())

h = Car("infinity", 8, "s3", 4, "blue", 300)
print(h.move())

#3 задание
class Circle:
    PI = 3.14
    def __init__(self, radius: int | float):
        self.radius = radius

    def area(self) -> int | float:
        return self.PI * self.radius ** 2

   def __sub__(self, circle2):
       res = self.area() - circle2.area()
       if res < 0:
           res = res * (-1)
       return res


c1 = Circle(20)
c2 = Circle(15)

print(c1.area())
print(c2.area())
print(c1.__sub__(c2))
