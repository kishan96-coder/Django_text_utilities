class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("hello my name is " + self.name)

p1 = Person("Amogh",19) 

p1.myFunc()