
class Dog:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def eat(self):
        return f"{self.name} has {self.weight}"
    def serve_people(self):
        return  f"{self.name}  serves people"
    def move(self):
        return  f"{self.name} has moved 3kilometers and has {self.weight}"
