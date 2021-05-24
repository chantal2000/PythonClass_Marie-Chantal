class Bank:
    def __init__(self,name,location):
        self.name=name
        self.location=location
    def save_money(self):
        return  self.name + "located in"+ self.location+ "save people's money"
    def money_transfer(self):
        return self.name + ' help people in transfering money'
    def advice_people(self):
        return  self.name + 'bank advice people on how to use money efficiently'