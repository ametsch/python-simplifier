from typing import Any
import base65536
import base64
import pyconverter as pc

__doc__ = """
    A class of functions to encode and decode between diferent number systems
"""

def toBase65536(val: Any) -> str:
    return base65536.encode(val)
toBase65536.__doc__ = "Encode val into base65536"

def fromBase65536(val: Any) -> str:
    return base65536.decode(val)
fromBase65536.__doc__ = 'Decode val from base65536 to a string'

def toBase64(val: Any) -> str:
    return base64.b64encode(val)
toBase64.__doc__ = 'Encode val into base64'

def fromBase64(val: str | bytes) -> str:
    return base64.b64decode(val)
fromBase64.__doc__ = 'Decodes val from base64 to a string'

def decToHex(val: float | int) -> str:
    return pc.doubletohex(val)
decToHex.__doc__ = 'Encodes a float or int into hexadecimal'

def hexToDec(val: str) -> float:
    return pc.hextodouble(val)
hexToDec.__doc__ = 'Decodes a hexadecimal encoded value into a float'

def decToBin(val: float | int) -> str:
    return pc.doubletobin(val)
decToBin.__doc__ = 'Encodes a float or int into binary'

def binToDec(val: str | bytes) -> float:
    return pc.bintodouble(val)
binToDec.__doc__ = 'Decodes binary to a float'

def hexToOct(val: str) -> str:
    return pc.hextooct(val)
hexToOct.__doc__ = 'Encodes a hexadecimal string into an octal string'

def decToOct(val: float | int) -> str:
    return pc.doubletooct(val)
decToOct.__doc__ = 'Encodes a float or int into an octal string'

def binToOct(val: str | bytes) -> str:
    return pc.bintooct(val)
binToOct.__doc__ = 'Encodes a binary string into an octal string'
