from io import IOBase
from ..typedefs import *
from ..exceptions import SegmentationFault
import sys

def pygets():
    return sys.stdin.readline()


def cgets(str: list):
    if not isinstance(str, list):
        raise TypeError("invalid string pointer")

    for i, c in enumerate(sys.stdin.readline()):
        if i >= len(str.s):
            raise SegmentationFault()

        str[i] = c

    return str

def cfgets(str: list, n: int, stream: FILE) -> list:
    if not isinstance(str, list):
        raise TypeError("invalid string pointer")

    if not isinstance(n, int):
        raise TypeError("n is not a n integer")

    if not isinstance(stream, IOBase):
        raise TypeError("invalid file stream")

    if n >= len(str):
        raise SegmentationFault()

    for i in range(n):
        str[i] = stream.read(1)

    return str

def pyfgets(n: int, stream: FILE) -> str:
    if not isinstance(n, int):
        raise TypeError("n is not a n integer")

    if not isinstance(stream, IOBase):
        raise TypeError("invalid file stream")

    return stream.read(n)