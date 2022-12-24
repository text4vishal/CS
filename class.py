class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person ("John", 36)

print ("Name: " + p1.name + "; Age: " + str(p1.age) +";")
