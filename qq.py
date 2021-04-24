class Human():
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        
    def bmi(self):
        return self.weight/ ((self.height/100)**2)
    
class Woman(Human):
    def __init__(self, name, weight, height, bust, waist, hip):
        super().__init__(name, weight, height)
        self.bust=bust
        self.waist=waist
        self.hip=hip
        
    def BWH(self):
        print("bust={}, waist={}, hip={}".format(self.bust,self.waist,self.hip))
        
class Man(Human):
    def __init__(self,nime,weight,height,military):
        super().__init__(nime,weight,height)
        self.military = military
        
    def description(self):
        if self.military:
            print('he is/was a solider')
        else:
            print("he is/was not a solider")