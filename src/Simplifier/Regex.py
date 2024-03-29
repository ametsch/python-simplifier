import re

__doc__ = '''
    A group of functions and constants to ease the use of regular expressions in python.
'''

isDecimal = re.compile(r'^[0-9\.]+$')
isHex = re.compile(r'^[0-9a-fA-F]+$')
isAlpha = re.compile(r'^[a-zA-Z]+$')
isAlphaNumeric = re.compile(r'^[0-9a-zA-Z]+$')
isBinary = re.compile(r'^[0-1]+$')
isOctal = re.compile(r'^[0-7]+$')
isBase64 = re.compile(r'^[0-9a-zA-Z\+/]+$')
isURLSafeBase64 = re.compile(r'^[0-9a-zA-Z\+_]+$')


def match(regex: re.Pattern, string: str) -> bool:
    if not re.match(regex, string) == None:
        return True
    else:
        return False


def match(regex: str, string: str) -> bool:
    if not re.match(re.compile(regex), string) == None:
        return True
    else:
        return False
