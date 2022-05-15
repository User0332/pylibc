from .._typecheck import getbuff
import sys
import os

def exit(status: int):
	if not isinstance(status, int):
		raise TypeError("exit() argument 'status' must be an integer")

	sys.exit(status)

def abort():
	sys.exit(1)

def getenv(name: str) -> str:
	string = getbuff(name)

	return os.environ.get(name)

def system(string: str) -> int:
	string = getbuff(string)

	return os.system(string)