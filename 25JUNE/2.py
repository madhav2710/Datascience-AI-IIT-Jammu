#lambda fn

square =lambda x: x*x
print(square(5))  # Output: 25

add=lambda x,y: x+y
print(add(3,4))

#class

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name},Age:{self.age}")
    
person1=person("Madhav",20)
person1.display()