from decimal import DivisionByZero
from numpy import float64, int64

class Fraction:
    def __init__(self):
        self.den = float64(1.0)
        self.num = float64(0.0)
    def __init__(self, num: float64 | int64, den: float64 | int64):
        if den == 0.0:
            raise DivisionByZero()
        else:
            self.den = den
            self.num = num
    
    def setNum(self, num: float64 | int64):
        self.num = num
    def setDen(self, den: float64 | int64):
        if den == 0.0:
            raise DivisionByZero()
        else:
            self.den = den
    
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    
    def eval(self):
        if self.den == 0.0:
            raise DivisionByZero()
        else:
            return float64(self.num/self.den)

    def __str__(self) -> str:
        return f"{self.num} / {self.den}"
