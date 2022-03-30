from numpy import float64, int64

class Fraction:
    def __init__(self):
        self.den = 0.0
        self.num = 0.0
    def __init__(self, num: float64 | int64, den: float64 | int64):
        self.den = den
        self.num = num
