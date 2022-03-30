import base65536
import base64
from numpy import float64, int64
import pyconverter as pc

class NumberSystems:
    def __init__(self):
        pass

    def toBase65536(self, val):
        return base65536.encode(val)
    def fromBase65536(self, val):
        return base65536.decode(val)
    
    def toBase64(self, val):
        return base64.b64encode(val)
    def fromBase64(self, val: str | bytes):
        return base64.b64decode(val)

    def decToHex(self, val: float64 | int64):
        return pc.doubletohex(val)
    def hexToDec(self, val: str):
        return pc.hextodouble(val)
    
    def decToBin(self, val: float64 | int64):
        return pc.doubletobin(val)
    def binToDec(self, val: str):
        return pc.doubletobin(val)

    def hexToOct(self, val: str):
        return pc.hextooct(val)

    def decToOct(self, val: float64 | int64):
        return pc.doubletooct(val)
