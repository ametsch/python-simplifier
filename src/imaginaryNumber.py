class imaginaryNumber:
    def __init__(self):
        self.a = 0
        self.b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def setA(self, a):
        self.a = a
    def setB(self, b):
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
