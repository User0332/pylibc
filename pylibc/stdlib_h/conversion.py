from .._typecheck import getbuff

def atof(s: str) -> float:
	s = getbuff(s)

	return float(s)

def atoi(s: str) -> int:
	s = getbuff(s)

	return int(s)

def pystrtoi(s: str, base: int = 10) -> int:
	s = getbuff(s)

	if not isinstance(base, int):
		raise TypeError("strtoi() argument 'base' must be an integer")

	return int(s, base)

def pystrtoul(s: str, base: int = 10) -> int:
	s = getbuff(s)

	if not isinstance(base, int):
		raise TypeError("strtoul() argument 'base' must be an integer")

	return int(s, base)+(2**32) #convert int to unsigned int

