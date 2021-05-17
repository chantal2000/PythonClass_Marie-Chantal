class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def accelerate(self,acceleration,speed):
        return acceleration+speed   
    def start(self):
        return "Vraaaaaaaaaaaaa"
    def park(self,kilometers):
        return kilometers