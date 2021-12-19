# rec class
class Rectangle : 
    def __init__(self, lenght, width):
      self.lenght = lenght
      self.width = width
    def calculatearea(self):
       area = self.lenght*self.width
       print(area)

#vehicle class

class Vehicle :
        def __init__(self, max_speed=0, mileage=0): 
          self.max_speed  = max_speed 
          self.mileage = mileage

#vehicle class without attrbts

class Vehicle2 : 
    def __init__(self):
        pass

#Bus 
bus = Vehicle()

