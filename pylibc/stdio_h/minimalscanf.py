from io import IOBase
from types import FunctionType
from ..typedefs import *
from ..exceptions import SegmentationFault
import sys

C_SCANF_FORMATS = {
	"%c" : lambda s: s[0],
	"%s" : str,
	"%d" : int,
	"%f" : float,
	"%b" : bytes
}

PY_SCANF_FORMATS = {
		"%s" : str,
		"%i" : int,
		"%d" : int,
		"%f" : float,
		"%b" : bytes,
		"%c" : lambda s: s[0]
}

def _parse_format(format: str, specifiers: dict) -> tuple[bool, int, FunctionType]:
	read_chars = True
	width_str = ""
	width = -1

	for i, char in enumerate(format):
		if i == 0:
			if char == '%':
				continue

			raise ValueError(f"Expected '%' at start of format string, got '{char}'")

		if i == 1:
			if char == '%':
				raise ValueError(f"Expected width or format type after '%', got double '%'")

			if '%'+char in specifiers:
				return read_chars, width, specifiers['%'+char]

			if char == '*':
				read_chars = False
				continue

			if char.isdigit():
				width_str += char
				continue

			raise ValueError(f"Unknown format specifier '%{char}'")

		if char.isdigit():
			width_str += char
			continue

		if width_str:
			width = int(width_str)
			width_str = ""

		if '%'+char in specifiers:
			return read_chars, width, specifiers['%'+char]

def pyscanf(format: str):
	return pyfscanf(sys.stdin, format)

def cscanf(format: str, var: list, *, BREAK_ON_WHITESPACE: bool=False):
	return cfscanf(sys.stdin, format, var, BREAK_ON_WHITESPACE=BREAK_ON_WHITESPACE)

def pyfscanf(stream: FILE, format: str):
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")


	read_chars, width, func = _parse_format(format, PY_SCANF_FORMATS)

	if not read_chars:
		stream.readline()
		return

	try:
		if width == -1:
			return func(stream.readline().replace("\n", "").split()[0])
		
		return func(stream.readline().replace("\n", "")[:width].split()[0])
	except ValueError:
		raise ValueError(f"Invalid input for format specifier '{format}'")


def cfscanf(stream: FILE, format: str, var: list, *, BREAK_ON_WHITESPACE: bool=False):
	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	read_chars, width, func = _parse_format(format, C_SCANF_FORMATS)

	if not read_chars:
		stream.readline()
		return

	if type(var) is not list:
		raise ValueError(f"Type of passed variable argument is not a pointer")

	if len(var) == 0:
		var.append(None)

	try:
		if BREAK_ON_WHITESPACE:
			if width == -1:
				res = func(stream.readline().replace("\n", "").split()[0])
			else:
				res = func(stream.readline().replace("\n", "")[:width].split()[0])
		else:
			if width == -1:
				res = func(stream.readline().replace("\n", ""))
			else:
				res = func(stream.readline().replace("\n", "")[:width])

		if func is str:
			if len(var) < len(res):
				raise SegmentationFault()

			for i, c in enumerate(res):
				var[i] = c
			

			return

		var[0] = res
	except ValueError:
		raise ValueError(f"Invalid input for format specifier '{format}'")