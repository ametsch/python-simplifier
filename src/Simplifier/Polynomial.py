import Simplifier
from Simplifier.Monomial import Monomial

class Polynomial:

    __doc__ = '''
        A class for a polynomial
    '''

    m = Monomial()
    def __init__(self, *args: Monomial):
        temp = []
        for i in args:
            if type(i) == type(self.m):
                temp.append(i)
        self.list = temp

    def __init__(self):
        self.list = []
    
    def add(self, monomial: Monomial) -> None:
        self.list.append(monomial)
        
    def remove(self, monomial: Monomial) -> None:
        self.list.remove(monomial)
    
    def __str__(self) -> str:
        out = ""
        for i in self.list:
            if i.getCoeff() < 0:
                out = out + f" - {i.getCoeff() * -1}X^{i.getExp()}"
            elif i.getCoeff() > 0:
                out = out + f" + {i.getCoeff()}X^{i.getExp()}"
            else:
                pass
        
        return out
    
    def dy_dx(self) -> Simplifier.Polynomial:
        temp = Polynomial()
        for i in self.list:
            temp.add(i.dy_dx())
        return temp
    dy_dx.__doc__ = 'A method to return the derivative of itself'

    def eval(self, val: float | int) -> float:
        temp = 0.0
        for i in self.list:
            temp += i.eval(val)
        return temp
    eval.__doc__ = 'A method to evaluate the value of the polynomial at X=val'