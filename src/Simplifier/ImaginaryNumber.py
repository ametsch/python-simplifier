class ImaginaryNumber:
    def __init__(self):
        self.a = 0
        self.b = 0
    def __init__(self, a: float | int, b: float | int):
        self.a = a
        self.b = b
    


    def setA(self, a: int | float):
        self.a = a
    def setB(self, b: int | float):
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
