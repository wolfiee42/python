class Animal():

    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Jack")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(cat.name)
cat.eat()
cat.sleep()
cat.speak()