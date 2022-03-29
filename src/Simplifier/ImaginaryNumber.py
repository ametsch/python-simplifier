class ImaginaryNumber:
    def __init__(self):
        self.a = 0
        self.b = 0
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def __init__(self, a: float, b: int):
        self.a = a
        self.b = b
    def __init__(self, a: int, b: float):
        self.a = a
        self.b = b
    


    def setA(self, a: int):
        self.a = a
    def setB(self, b: int):
        self.b = b
    def setA(self, a: float):
        self.a = a
    def setB(self, b: float):
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
