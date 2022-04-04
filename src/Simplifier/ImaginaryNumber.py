from numpy import float64, int64

class ImaginaryNumber:
    __doc__ = """
        a class to store the value of a complex number in the form a+bi
    """
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        
    def __init__(self, a: float64 | int64, b: float64 | int64):
        self.a = a
        self.b = b

    def setA(self, a: int64 | float64) -> None:
        self.a = a

    def setB(self, b: int64 | float64) -> None:
        self.b = b
        
    def getA(self) -> float64 | int64:
        return self.a

    def getB(self) -> float64 | int64:
        return self.b

    def __str__(self) -> str:
        if self.b > 0.0:
            return f"{self.a}+{self.b}i"
        elif self.b < 0.0:
            return f"{self.a}-{self.b * -1.0}i"
        else:
            return ""
