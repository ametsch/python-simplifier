
class Simplifier:
    def __init__(self):
        pass
    
    pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006
    sqrt2 = 1.4142135623730950488016887242096980785696718753769480731766
    sqrt3 = 1.7320508075688772935274463415058723669428052538103806280558069794
    sqrt10 = 3.1622776601683793319988935444327185337195551393252168268575048527

    def p(self, val):
        print(val)
    def pf(self, val: str, *args):
        print(str.format(val, args))
    def printf(self, val: str, *args):
        print(str.format(val, args))
    
    def nthrt(self, val: float | int, n: float | int):
        return val**(1.0/n)
    def curt(self, val: float | int):
        return val**(1.0/3.0)
    
    def isEven(self, val: int):
        if val % 2 == 0:
            return True
        else:
            return False
    def isOdd(self, val: int):
        if val % 2 == 1:
            return True
        else:
            return False

