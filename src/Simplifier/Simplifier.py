from numpy import float128, float256, float64, int64

class Simplifier:
    def __init__(self):
        pass
    
    __doc__ = """
    this class contains some mathematical constants and some functions to ease python programming/scripting
    """

    pi = float256(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006)
    pi.__doc__ = "the constant of pi"

    sqrt2 = float128(1.4142135623730950488016887242096980785696718753769480731766)
    sqrt2.__doc__ = "the constant of the square root of 2"

    sqrt3 = float128(1.7320508075688772935274463415058723669428052538103806280558069794)
    sqrt3.__doc__ = "the constant of the square root of 3"

    sqrt10 = float128(3.1622776601683793319988935444327185337195551393252168268575048527)
    sqrt10.__doc__ = "the constant of the square root of 10"

    e = float256(2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424)
    e.__doc__ = "the constant of euler's number"

    oneThird = float256(float256(1.0)/float256(3.0))
    oneThird.__doc__ = "the constant of one third"

    def p(self, val) -> None:
        print(val)
    p.__doc__ = "equivelant to 'print(val)'"

    def pf(self, val: str, *args) -> None:
        print(str.format(val, args))
    pf.__doc__ = "equivelant to 'print(str.format(val, *args))'"

    def printf(self, val: str, *args) -> None:
        print(str.format(val, args))
    printf.__doc__ = "equivelant to 'print(str.format(val, *args))'"
    
    def nthrt(self, val: float64 | int64, n: float64 | int64) -> float64 | int64:
        return val**(1.0/n)
    nthrt.__doc__ = "take the nth root of val"

    def curt(self, val: float64 | int64) -> float64:
        return val**(self.oneThird)
    curt.__doc__ = "take the cubed root of val"
    
    def isEven(self, val: int64) -> bool:
        if val % 2 == 0:
            return True
        else:
            return False
    isEven.__doc__ = "return if val is even"
    
    def isOdd(self, val: int64) -> bool:
        if val % 2 == 1:
            return True
        else:
            return False
    isOdd.__doc__ = "return if val is odd"

