from types.Monomial import Monomial


class Polynomial:
    def __init__(self, *args):
        temp = []
        for i in args:
            temp.append(i)
        self.list = temp
    def __init__(self):
        self.list = []
    
    def add(self, monomial: Monomial):
        self.list.append(monomial)
    def remove(self, monomial: Monomial):
        self.list.remove(monomial)
    
    def __str__(self):
        out = ""
        for i in self.list:
            if i.getCoeff() < 0:
                out = out + f" - {i.getCoeff() * -1}X^{i.getExp()}"
            elif i.getCoeff() > 0:
                out = out + f" + {i.getCoeff()}X^{i.getExp()}"
            else:
                pass
        
        return out
    
    def dy_dx(self):
        temp = Polynomial()
        for i in self.list:
            temp.add(i.dy_dx())
        return temp


