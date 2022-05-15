from ..constants import *
from .._typecheck import getbuff

def atof(s: str) -> float:
	s = getbuff(s)

	return float(s)

def atoi(s: str) -> int:
	s = getbuff(s)

	return int(s)

def pystrtol(s: str, base: int = 10) -> int:
	s = getbuff(s)

	if not isinstance(base, int):
		raise TypeError("strtoi() argument 'base' must be an integer")

	return int(s, base)

def pystrtoul(s: str, base: int = 10) -> int:
	s = getbuff(s)

	if not isinstance(base, int):
		raise TypeError("strtoul() argument 'base' must be an integer")

	return int(s, base)+(2**32) #convert int to unsigned int

def cstrtol(s: str, endptr: list, base: int = 10) -> int:
	to_convert = ""
	
	s = getbuff(s)

	if not isinstance(endptr, list):
		raise TypeError("strtol() argument 'endptr' must be a list")

	if not isinstance(base, int):
		raise TypeError("strtol() argument 'base' must be an integer")

	endptr.clear()

	for i, char in enumerate(s):
		if char == '-' and i == 0:
			to_convert+=char
		elif char.isdigit():
			to_convert+=char
		else:
			endptr.append(char)
			break

	if not endptr: endptr.append(NULL)

	return int(to_convert, base)

def cstrtoul(s: str, endptr: list, base: int = 10) -> int:
	to_convert = ""

	s = getbuff(s)

	if not isinstance(endptr, list):
		raise TypeError("strtoul() argument 'endptr' must be a list")

	if not isinstance(base, int):
		raise TypeError("strtoul() argument 'base' must be an integer")

	endptr.clear()

	for i, char in enumerate(s):
		if char == '-' and i == 0:
			to_convert+=char
		elif char.isdigit():
			to_convert+=char
		else:
			endptr.append(char)
			break

	if not endptr: endptr.append(NULL)

	return int(to_convert, base)+(2**32) #convert int to unsigned int