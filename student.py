class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return  f"{self.name} is talkative"
    def eat(self):
        return  f"Peope with {self.age} eat food a lot"
