from ..constants import *
from ..typedefs import *
from .._typecheck import getbuff

def __atxx_convert(s: str, func):
	try:
		return func(getbuff(s))
	except ValueError:
		return 0


def atof(s: str) -> float:
	return __atxx_convert(s, float)

def atoi(s: str) -> int:
	return __atxx_convert(s, int)

def atol(s: str) -> long_int:
	return __atxx_convert(s, long_int)

def pystrtol(s: str, base: int=10) -> long_int:
	s = getbuff(s)

	if not isinstance(base, int):
		raise TypeError("strtoi() argument 'base' must be an integer")

	return long_int(s, base)

def pystrtoul(s: str, base: int=10) -> uint:
	s = getbuff(s)

	if not isinstance(base, int):
		raise TypeError("strtoul() argument 'base' must be an integer")

	return int(s, base)+(2**32) #convert int to unsigned int

def strtol(s: str, endptr: list, base: int=10) -> long_int:
	to_convert = ""
	
	s = getbuff(s)

	if not isinstance(endptr, list):
		raise TypeError("strtol() argument 'endptr' must be a list")

	if not isinstance(base, int):
		raise TypeError("strtol() argument 'base' must be an integer")

	endptr.clear()

	for i, char in enumerate(s):
		if char in ('-', '+') and i == 0:
			to_convert+=char
		elif char.isdigit():
			to_convert+=char
		else:
			endptr.append(char)
			break

	if not endptr: endptr.append(NULL)

	return long_int(to_convert, base)

def strtoul(s: str, endptr: list, base: int=10) -> uint:
	to_convert = ""

	s = getbuff(s)

	if not isinstance(endptr, list):
		raise TypeError("strtoul() argument 'endptr' must be a list")

	if not isinstance(base, int):
		raise TypeError("strtoul() argument 'base' must be an integer")

	endptr.clear()

	for i, char in enumerate(s):
		if char in ('-', '+') and i == 0:
			to_convert+=char
		elif char.isdigit():
			to_convert+=char
		else:
			endptr.append(char)
			break

	if not endptr: endptr.append(NULL)

	return int(to_convert, base)+(2**32) #convert int to unsigned int

def strtod(s: str, endptr: list, base: int=10):
	to_convert = ""

	s = getbuff(s)

	if not isinstance(endptr, list):
		raise TypeError("strtoul() argument 'endptr' must be a list")

	if not isinstance(base, int):
		raise TypeError("strtoul() argument 'base' must be an integer")

	endptr.clear()

	for i, char in enumerate(s):
		if char in ('-', '+') and i == 0:
			to_convert+=char
		elif char.isdigit():
			to_convert+=char
		elif char == '.' and '.' not in to_convert:
			to_convert+=char
		else:
			endptr.append(char)
			break

	if not endptr: endptr.append(NULL)

	return float(to_convert, base)

strtof, strtold = strtod, strtod
strtoll = strtol
stroull = strtoul