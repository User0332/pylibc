from io import TextIOWrapper as struct_IO_FILE

class uint(int):
	def __init__(self, value):
		self = value+(2**32)

size_t = int
FILE = struct_IO_FILE
long_int = int
char = int
uchar = uint
double = float