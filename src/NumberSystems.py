import base65536
import pyconverter as pc

class NumberSystems:
    def __init__(self):
        pass

    def toBase65536(self, val):
        return base65536.encode(val)
    def fromBase65536(self, val):
        return base65536.decode(val)

    def decToHex(self, val: float):
        return pc.doubletohex(val)
    def hexToDec(self, val: str):
        return pc.hextodouble(val)
    
    def decToBin(self, val: float):
        return pc.doubletobin(val)
    def binToDec(self, val: str):
        return pc.doubletobin(val)

    def hexToOct(self, val: str):
        return pc.hextooct(val)

    def decToOct(self, val: float):
        return pc.doubletooct(val)
