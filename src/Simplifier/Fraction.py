from numpy import float64, int64

class Fraction:
    def __init__(self):
        self.den = 0.0
        self.num = 0.0
    def __init__(self, num: float64 | int64, den: float64 | int64):
        self.den = den
        self.num = num
    
    def setNum(self, num: float64 | int64):
        self.num = num
    def setDen(self, den: float64 | int64):
        self.den = den
    
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    
    def eval(self):
        return float64(self.num/self.den)
