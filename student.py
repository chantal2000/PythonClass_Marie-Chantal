class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return  self.name +"is talkative"
    def eat(self):
        return  "Peope with " + self.age+ "eats food a lot"
