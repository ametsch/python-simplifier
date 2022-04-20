import imp
from Simplifier.ImaginaryNumber import ImaginaryNumber


class ImaginaryNumber:
    __doc__ = """
        a class to store the value of a complex number in the form a+bi
    """
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        
    def __init__(self, a: float | int, b: float | int):
        self.a = a
        self.b = b

    def setA(self, a: int | float) -> None:
        self.a = a

    def setB(self, b: int | float) -> None:
        self.b = b
        
    def getA(self) -> float:
        return self.a

    def getB(self) -> float:
        return self.b

    def __str__(self) -> str:
        if self.b > 0.0:
            return f"{self.a}+{self.b}i"
        elif self.b < 0.0:
            return f"{self.a}-{self.b * -1.0}i"
        else:
            return ""

    def add(self, val: ImaginaryNumber) -> ImaginaryNumber:
        a = self.getA() + val.getA()
        b = self.getB() + val.getB()
        return ImaginaryNumber(a, b)