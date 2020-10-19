class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Zebra(Animal):
    def __init__(self, name, age, info):
        self.name = name
        self.age = age
        self.info = info
    def __str__(self):
        return "Hello, i am " + self.__class__.__name__ + ". My name is " + self.name + ". I am " + self.age +" years old and I am "+ self.info + '.'
class Dolphin(Animal):
    def __init__(self, name, age, info):
        self.name = name
        self.age = age
        self.info = info
    def __str__(self):
        return "Hello, i am " + self.__class__.__name__ + ". My name is " + self.name + ". I am " + self.age + " years old and I am " + self.info + "."

a = Zebra('Zyoma', '20', 'fakishnik')
b = Dolphin('Zhenya' , '30', 'tired of living')
print(a)
print(b)