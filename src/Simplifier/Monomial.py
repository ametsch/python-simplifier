from numpy import float64, int64
import Simplifier

class Monomial:
    def __init__(self, coeff: float64 | int64, exp: int64):
        self.coeff = coeff
        self.exp = exp
        
    def __init__(self):
        self.coeff = 0.0
        self.exp = 0.0
    
    def __str__(self) -> str:
        return f"({self.coeff})X^({self.exp})"
    
    def getCoeff(self) -> float64:
        return self.coeff

    def getExp(self) -> int64:
        return self.exp

    def setCoeff(self, coeff: float64):
        self.coeff = coeff

    def setExp(self, exp: int64) -> None:
        self.exp = exp

    def eval(self, val: float64 | int64) -> float64:
        return self.coeff * pow(val, self.exp)
    eval.__doc__ = "a method which evaluates the monomial where X=val"

    def dy_dx(self) -> Simplifier.Monomial:
        return Monomial(self.coeff*self.exp, self.exp-1)
    dy_dx.__doc__ = "return a Monomial that is the first derivative of itself"
