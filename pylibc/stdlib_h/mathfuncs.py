import random
from typing import Type
from ..constants import *

class div_t:
	def __init__(self, quot, rem):
		self.quot = quot
		self.rem = rem

ldiv_t, lldiv_t = div_t, div_t

def srand(seed: int):
	if not isinstance(seed, int):
		raise TypeError("srand() argument 'seed' should be an int")

	random.seed = seed

def rand() -> int:
	return random.randint(0, RAND_MAX)

def abs(x: int) -> int: #provide our own definition for abs
	if not isinstance(abs, int):
		raise TypeError("abs() argument 'abs' should be an int")

	return __builtins__['abs'](x)

def __div_base(numer: int, denom: int, struct: Type) -> div_t:
	if not isinstance(numer, int):
		raise TypeError("div() argument 'numer' should be an int")

	if not isinstance(denom, int):
		raise TypeError("div() argument 'denom' should be an int")

	return struct(*divmod(numer, denom))

def div(numer: int, denom: int):
	return __div_base(numer, denom, div_t)
	
def ldiv(numer: int, denom: int):
	return __div_base(numer, denom, ldiv_t)
	
def lldiv(numer: int, denom: int):
	return __div_base(numer, denom, lldiv_t)

labs, llabs = abs, abs