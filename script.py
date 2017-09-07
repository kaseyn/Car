class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()

    def displayAll(self):
        print "Price: $" +str(self.price)
        print "Speed: " +str(self.speed)+ " MPH"
        print "Mileage: " +str(self.mileage)+ " MPG"
        print "Fuel: " +self.fuel
        print "Tax: " +str(self.tax)
        print "\n"

car1 = Car(9000,60,"Full",22) 
car2 = Car(2100,30,"Full",17) 
car3 = Car(5500,70,"Empty",98) 
car4 = Car(91000,160,"Full",8) 
car5 = Car(300,21,"Half",2700)
car6 = Car(40000, 45, "Empty", 206007)