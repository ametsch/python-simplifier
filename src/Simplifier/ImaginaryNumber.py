from numpy import float64, int64

class ImaginaryNumber:
    def __init__(self):
        self.a = 0
        self.b = 0
    def __init__(self, a: float64 | int64, b: float64 | int64):
        self.a = a
        self.b = b
    


    def setA(self, a: int64 | float64):
        self.a = a
    def setB(self, b: int64 | float64):
        self.b = b
        
    def getA(self):
        return self.a
    def getB(self):
        return self.b

    def __str__(self):
        if self.b > 0:
            return f"{self.a}+{self.b}i"
        elif self.b < 0:
            return f"{self.a}-{self.b * -1}i"
        else:
            return ""
