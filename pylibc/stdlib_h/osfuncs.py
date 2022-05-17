from types import FunctionType
from .._typecheck import getbuff
import os
import atexit as _atexit

def exit(status: int):
	if not isinstance(status, int):
		raise TypeError("exit() argument 'status' must be an integer")

	os._exit(status)

def abort():
	os._exit(1)

def getenv(name: str) -> str:
	string = getbuff(name)

	return os.environ.get(name)

def system(string: str) -> int:
	string = getbuff(string)

	return os.system(string)

def atexit(func: FunctionType) -> None:
	_atexit.register(func)

def pyatexit_args(func: FunctionType, *args, **kwargs) -> None:
	_atexit.register(func, *args, **kwargs)