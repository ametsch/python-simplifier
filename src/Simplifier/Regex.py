import re

__doc__ = """
    A group of functions and constants to ease the use of regular expressions in python.
"""

isDecimal = re.compile(r"^[0-9]+$")
isHex = re.compile(r"^[0-9a-fA-F]+$")
isAlpha = re.compile(r"^[a-zA-Z]+$")
isAlphaNumeric = re.compile(r"^[0-9a-zA-Z]+$")
