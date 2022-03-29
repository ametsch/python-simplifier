class Monomial:
    def __init__(self, coeff: float | int, exp: float | int):
        self.coeff = coeff
        self.exp = exp
    def __init__(self):
        self.coeff = 0.0
        self.exp = 0.0
    
    def __str__(self):
        return f"{self.coeff}X^{self.exp}"
    
    def getCoeff(self):
        return self.coeff
    def getExp(self):
        return self.exp
    def setCoeff(self, coeff: float | int):
        self.coeff = coeff
    def setExp(self, exp: float | int):
        self.exp = exp

    def eval(self, val: float | int):
        return self.coeff * pow(val, self.exp)

    def dy_dx(self):
        return Monomial(self.coeff*self.exp, self.exp-1)