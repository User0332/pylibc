from ..typedefs import *
from .._typecheck import *
from ..constants import *
from ..exceptions import SegmentationFault		

def mbtowc(pwc: list, pmb: str, max: size_t):
	char = ""

	if not isinstance(pwc, list):
		raise TypeError("mbtowc() argument 'pwc' must be a pointer")

	if not isinstance(max, size_t):
		raise TypeError("mbtowc() argument 'max' must be a size_t")

	if not isinstance(pmb, str) or not isinstance(pmb, list):
		raise TypeError("mbtowc() argument 'pmb' must be a pointer to a multibyte character")

	if max > len(pmb):
		raise SegmentationFault()

	pmb = pmb[:max]

	pmb = getbuff(pmb)

	pwc.clear()


	for c in s:
		char+=bin(ord(c))

	try: pwc.append(chr(int(char, base=2)))
	except ValueError, OverflowError: return -1

	return 0

def mblen(s: str, n: size_t) -> int:
	if s == NULL:
		return 0

	c = []
	if mbtowc(c, s, n) == -1:
		return -1
	else:
		return n

