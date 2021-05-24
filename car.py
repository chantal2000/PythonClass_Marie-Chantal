class Car:
    def __init__(self,acceleration,speed):
        self.acceleration=acceleration
        self.speed=speed
    def accelerate(self):
        return self.acceleration+self.speed   
    def start(self):
        return self.speed + "Vraaaaaaaaaaaaa"
    def park(self,kilometers):
        return self.speed +"Kilometers"