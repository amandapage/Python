class Money:
    def __init__(self,dollar,cents= 0):
        self.dollar = dollar
        self.cents = cents
        self.cleanUp()

    def cleanUp(self):
        if self.cents >= 100 and self.dollar >=0:
            self.dollar += self.cents//100
            self.cents = self.cents%100

        elif self.cents < 0 and self.dollar >=0:
            if self.cents > -100:
                self.dollar -= 1
                self.cents += 100
            else:
                self.dollar += self.cents//100
                self.cents = self.cents%100

        elif self.dollar < 0 and self.cents > 0:
            self.dollar += 1
            self.cents = self.cents - 100

        elif self.dollar < 0 and self.cents < 0:    
            if self.cents <= -100:
                self.dollar += self.cents//100
                print(((self.cents*-1)%100)*-1)
                self.cents = ((self.cents*-1)%100)*-1
        
    def addPenny(self):
        self.cents += 1
        self.cleanUp()
       
    def __add__(self, other):
        newDol = self.dollar + other.dollar
        newCen = self.cents + other.cents
        return Money(newDol,newCen)
            
    def __sub__(self,other):
        newDol = self.dollar - other.dollar
        newCen = self.cents - other.cents
        return Money(newDol,newCen)

    def __repr__(self):
        if self.dollar >= 0 and self.cents >= 0:
            return "$" + str(self.dollar) + "." + ("{:02d}".format(self.cents))
        else:
            return "-$" + str(abs(self.dollar)) + "." + ("{:02d}".format(abs(self.cents)))
        
