class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):

    def speak(self):
        return f"{self.name} says Woof!"

    def shakePaw(self):
        print("Жму лапу")


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
    def purr(self):
        print("мурр")

class KotoPES(Dog, Cat):

    def speak(self):
        return f"{self.name} says MeowWoof!"

dog = Dog("Мухтар")
cat = Cat("Барсик")
kotopes = KotoPES("КОТОПЕС")

print(dog.speak())
print(cat.speak())
print(kotopes.speak())

cat.purr()
kotopes.purr()
print(kotopes.a)