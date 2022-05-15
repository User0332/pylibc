from io import IOBase
from ..typedefs import *
from ..constants import EOF
import sys

def getchar() -> int:
	return getc(sys.stdin)

def getc(stream: FILE) -> int:
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	try:
		return ord(stream.read(1))
	except ValueError:
		return EOF