from io import IOBase
from ..typedefs import *
from .._typecheck import getbuff
import sys
import random

def printf(_Format: str, *varargs, USE_ONLY_KNOWN_FORMAT_SPECIFIERS=False, WARNINGS=False) -> int:
	return vprintf(_Format, list(varargs), USE_ONLY_KNOWN_FORMAT_SPECIFIERS=USE_ONLY_KNOWN_FORMAT_SPECIFIERS, WARNINGS=WARNINGS)

def fprintf(stream: FILE, _Format: str, *varargs, USE_ONLY_KNOWN_FORMAT_SPECIFIERS=False, WARNINGS=False) -> int:
	return vfprintf(stream, _Format, list(varargs), USE_ONLY_KNOWN_FORMAT_SPECIFIERS=USE_ONLY_KNOWN_FORMAT_SPECIFIERS, WARNINGS=WARNINGS)

def vprintf(_Format: str, arg: list[str], *, USE_ONLY_KNOWN_FORMAT_SPECIFIERS=False, WARNINGS=False) -> int:
	return vfprintf(sys.stdout, _Format, arg, USE_ONLY_KNOWN_FORMAT_SPECIFIERS=USE_ONLY_KNOWN_FORMAT_SPECIFIERS, WARNINGS=WARNINGS)

def vfprintf(stream: FILE, _Format: str, arg: list[str], *, USE_ONLY_KNOWN_FORMAT_SPECIFIERS=False, WARNINGS=False) -> int:
	va_list_counter = 0
	format_encountered = False
	writestr = ""
	rand_arg = False

	if not isinstance(stream, IOBase):
		raise TypeError("invalid file stream")

	for char in _Format:
		if format_encountered:
			if char == "%":
				writestr+="%"
			else:
				if va_list_counter >= len(arg) and WARNINGS:
					rand_arg = True
				else:
					var = arg[va_list_counter]	
				
				if char == "s":
					if rand_arg:
						var = ''.join([chr(random.randint(0, 5000)) for x in range(random.randint(7, 32))])
					var = getbuff(var, err="Format specifier %s expects a string argument")
				elif char == "i":
					if rand_arg:
						var = random.randint(0, 5000)
					elif not isinstance(var, int):
						raise ValueError("Format specifier %i expects an integer argument")
				elif char in ("d", "f"):
					if rand_arg:
						var = random.uniform(0, 10000)
					elif not isinstance(var, float):
						raise ValueError(f"Format specifier %{char} expects a floating-point number argument")
				elif char == "c":
					if rand_arg:
						var = chr(random.randint(0, 5000))
					elif not ((isinstance(var, str)) and (len(var) == 1)) and (not isinstance(var, int)):
						raise ValueError("Format specifier %c expects a character argument")
					if isinstance(var, int):
						var = chr(var)
				elif char == " ":
					raise ValueError("No format specified after % symbol")
				elif USE_ONLY_KNOWN_FORMAT_SPECIFIERS:
					raise ValueError(f"Unknown format '%{char}'")
				
				if rand_arg:
					rand_arg = False
					
				writestr+=str(var)
				va_list_counter+=1

			format_encountered = False
		elif char == "%":
			format_encountered = True
		else:
			writestr+=char

	if (va_list_counter < len(arg)) and WARNINGS:
		print("Warning at call to printf: unnecessary varargs")
	
	stream.write(writestr)

	return len(writestr)