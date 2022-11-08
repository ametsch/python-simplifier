from decimal import DivisionByZero

class Fraction:

    __doc__ = '''
        A class for a fraction
    '''

    def __init__(self):
        self.den = float(1.0)
        self.num = float(0.0)

    def __init__(self, num: float | int, den: float | int):
        if den == 0.0:
            raise DivisionByZero(den)
        else:
            self.den = den
            self.num = num
    
    def setNum(self, num: float | int) -> None:
        self.num = num

    def setDen(self, den: float | int) -> None:
        if den == 0.0:
            raise DivisionByZero(den)
        else:
            self.den = den
    
    def getNum(self) -> float:
        return self.num

    def getDen(self) -> float:
        return self.den
    
    def eval(self) -> float:
        if self.den == 0.0:
            raise DivisionByZero(self.den)
            pass
        else:
            return float(self.num/self.den)
    eval.__doc__ = 'Evaluates the fraction and returns a float value'

    def __str__(self) -> str:
        return f'{self.num} / {self.den}'
