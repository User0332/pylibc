from .constants import NULL

def getbuff(buff: list, *, err="invalid char buffer") -> str:
	if isinstance(buff, str):
		return buff

	if not isinstance(buff, list):
		raise TypeError(err)
	
	__str = ""
	for c in buff:
		if isinstance(c, str) and len(c) == 1:
			__str += c
		elif isinstance(c, int):
			__str += chr(c)
		elif c is NULL:
			break
		else:
			raise TypeError(err)


	return __str

