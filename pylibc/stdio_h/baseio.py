from io import IOBase
from ..typedefs import *
from ..exceptions import SegmentationFault
import os


SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

def fopen(filename: str, mode: str) -> FILE:
	return open(filename, mode)

def fdopen(fd: int, mode: str) -> FILE:
	return os.fdopen(fd, mode)

def fseek(stream: FILE, offset: int, whence: int) -> int:
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file pointer")

	if not isinstance(offset, int):
		raise TypeError("offset must be an int")

	if not isinstance(whence, int):
		raise TypeError("whence must be an int")

	try:
		stream.seek(offset, whence)
	except ValueError:
		return 1
	
	return 0

def fwrite(ptr: str, size: size_t, nmemb: size_t, stream: FILE) -> int:
	write_str = ""

	if len(ptr) < nmemb:
		raise SegmentationFault()

	if not isinstance(size, int) or not isinstance(nmemb, int):
		raise TypeError("size and nmemb are not integers/size_t")
	
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	for i in range(nmemb):
		#only get the first {size} bits of the character
		c = chr(int(bin(ord(ptr[i]))[:size], 2))

		write_str+=c

	stream.write(write_str)

	return len(write_str)

def cfread(ptr: str, size: size_t, nmemb: size_t, stream: FILE) -> int:
	chars_read = 0

	if len(ptr) < nmemb:
		raise SegmentationFault()

	if not isinstance(size, int) or not isinstance(nmemb, int):
		raise TypeError("size and nmemb are not integers/size_t")
	
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")
	
	if not isinstance(ptr, str):
		raise TypeError("invalid string pointer")

	for i in range(nmemb):
		char = stream.read(size)
		ptr[i] = char
		chars_read+=1

	return chars_read

def pyfread(size: size_t, nmemb: size_t, stream: FILE) -> str:
	read_str = ""

	if not isinstance(size, int) or not isinstance(nmemb, int):
		raise TypeError("size and nmemb are not integers/size_t")
	
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	for i in range(nmemb):
		read_str+=stream.read(size)

	return read_str

def fclose(stream: FILE) -> int:
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	if stream.closed:
		return 1
	else:
		stream.close()
		return 0




	

