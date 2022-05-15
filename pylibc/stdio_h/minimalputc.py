from io import IOBase
from ..typedefs import *
import sys

def putchar(char: int):
	return fputc(char, sys.stdout)

def fputc(char: int, stream: FILE) -> int:
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	if isinstance(char, int):
		char = chr(char)
	elif not isinstance(char, str) or (isinstance(char, str) and len(char) != 1):
		raise TypeError("invalid character")
		

	try:
		stream.write(char)
	except ValueError:
		return 1

	return 0