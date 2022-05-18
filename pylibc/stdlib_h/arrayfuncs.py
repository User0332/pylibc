from types import FunctionType
from copy import deepcopy
from ..typedefs import *
from ..constants import *
from ..exceptions import SegmentationFault

def bsearch(key: list, base: list, num: size_t, size: size_t, compar: FunctionType) -> list:
	'''Perform a binary search in an array. Note that the argument 'size' is required for uniformity but never used.'''

	if not isinstance(key, list) or key == NULL:
		raise TypeError("bsearch() argument 'key' must be a non-null pointer")

	if not isinstance(base, list):
		raise TypeError("bsearch() argument 'base' must be a list")

	if not isinstance(num, size_t):
		raise TypeError("bsearch() argument 'num' must be a size_t")

	if not isinstance(size, size_t):
		raise TypeError("bsearch() argument 'size' must be a size_t")

	if not isinstance(compar, bsearch.__class__):
		raise TypeError("bsearch() argument 'compar' must be a function pointer")

	if num > len(base)-1: raise SegmentationFault()
	arr = deepcopy(base[:num])

	while arr:
		idx = int(len(arr)-1/2) #convert to in in case the number of elements is odd
		item = [arr[idx]]

		# if compar accepts less or more arguments, let it throw the error.
		# we don't want to wrap this in a try catch in case an exception occurs in compar()
		move = compar(key, item)
		if not isinstance(move, int):
			raise TypeError("bsearch() argument 'compar' must return an int")

		if move > 0: arr = arr[idx:]
		elif move < 0: arr = arr[:idx]
		else:
			return item

	return NULL # if the searching array is empty, i.e. no item was found, return NULL

def qsort(base: list, num: size_t, size: size_t, compar: FunctionType) -> None:
	'''Sorts an array. Note that the argument 'size' is required for uniformity but never used.'''

	if not isinstance(base, list):
		raise TypeError("qsort() argument 'base' must be a list")

	if not isinstance(num, size_t):
		raise TypeError("qsort() argument 'num' must be a size_t")

	if not isinstance(size, size_t):
		raise TypeError("qsort() argument 'size' must be a size_t")

	if not isinstance(compar, bsearch.__class__):
		raise TypeError("qsort() argument 'compar' must be a function pointer")

	if num > len(base)-1: raise SegmentationFault()

	_sorted = sorted(base[:num], key=compar)

	base.clear()

	base.extend(_sorted)


	
