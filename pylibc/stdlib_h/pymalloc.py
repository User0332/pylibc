from ..typedefs import *

def malloc(size: size_t) -> list:
	'''NOTE: This function does not allocate bytes. Instead, it allocates list elements.'''
	if not isinstance(size, size_t):
		raise TypeError("size must be a size_t")

	return [None]*size

def free(ptr: list):
	if not isinstance(ptr, list):
		raise TypeError("ptr must be a list")

	del ptr

def calloc(size: size_t) -> list:
	ptr = malloc(size)
	for i in range(size):
		ptr[i] = 0

	return ptr

def realloc(ptr: list, size: size_t) -> list:
	if not isinstance(ptr, list):
		raise TypeError("ptr must be a list")

	if not isinstance(size, size_t):
		raise TypeError("size must be a size_t")

	if len(ptr) > size:
		return ptr[:size]
	
	return+[None]*(size-len(ptr))