from io import IOBase
from .._typecheck import getbuff
from ..typedefs import *
import sys

def puts(s: str) -> int:
	return fputs(s, sys.stdout)

def fputs(s: str, stream: FILE) -> int:

	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	s = getbuff(s)

	try:
		stream.write(s)
		stream.flush()
	except ValueError:
		return 1

	return 0