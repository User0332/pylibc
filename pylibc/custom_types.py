from .exceptions import SegmentationFault

class _FreedPointer:
	def __getattr__(self, name: str) -> None:
		raise SegmentationFault()

	def __getattribute__(self, name: str) -> None:
		raise SegmentationFault()

	def __setattr__(self, name: str, value) -> None:
		raise SegmentationFault()

	def __delattr__(self, name: str) -> None:
		raise SegmentationFault()

	def __repr__(self) -> None:
		raise SegmentationFault()

	def __add__(self, other) -> None:
		raise SegmentationFault()

	def __sub__(self, other) -> None:
		raise SegmentationFault()

	def __mul__(self, other) -> None:
		raise SegmentationFault()

	def __floordiv__(self, other) -> None:
		raise SegmentationFault()

	def __mod__(self, other) -> None:
		raise SegmentationFault()

	def __divmod__(self, other) -> None:
		raise SegmentationFault()

	def __pow__(self, other) -> None:
		raise SegmentationFault()

	def __lshift__(self, other) -> None:
		raise SegmentationFault()

	def __rshift__(self, other) -> None:
		raise SegmentationFault()

	def __and__(self, other) -> None:
		raise SegmentationFault()

	def __xor__(self, other) -> None:
		raise SegmentationFault()

	def __or__(self, other) -> None:
		raise SegmentationFault()

	def __iadd__(self, other) -> None:
		raise SegmentationFault()

	def __isub__(self, other) -> None:
		raise SegmentationFault()

	def __imul__(self, other) -> None:
		raise SegmentationFault()

	def __ifloordiv__(self, other) -> None:
		raise SegmentationFault()

	def __imod__(self, other) -> None:
		raise SegmentationFault()

	def __ipow__(self, other) -> None:
		raise SegmentationFault()

	def __ilshift__(self, other) -> None:
		raise SegmentationFault()

	def __irshift__(self, other) -> None:
		raise SegmentationFault()

	def __iand__(self, other) -> None:
		raise SegmentationFault()

	def __ixor__(self, other) -> None:
		raise SegmentationFault()

	def __ior__(self, other) -> None:
		raise SegmentationFault()
	
	def __neg__(self) -> None:
		raise SegmentationFault()

	def __pos__(self) -> None:
		raise SegmentationFault()

	def __abs__(self) -> None:
		raise SegmentationFault()

	def __invert__(self) -> None:
		raise SegmentationFault()

	def __complex__(self) -> None:
		raise SegmentationFault()

	def __int__(self) -> None:
		raise SegmentationFault()

	def __float__(self) -> None:
		raise SegmentationFault()

	def __oct__(self) -> None:
		raise SegmentationFault()

	def __hex__(self) -> None:
		raise SegmentationFault()

	def __index__(self) -> None:
		raise SegmentationFault()

	def __coerce__(self, other) -> None:
		raise SegmentationFault()

	def __enter__(self) -> None:
		raise SegmentationFault()

	def __exit__(self, exc_type, exc_value, traceback) -> None:
		raise SegmentationFault()

	def __trunc__(self) -> None:
		raise SegmentationFault()

	def __round__(self) -> None:
		raise SegmentationFault()

	def __floor__(self) -> None:
		raise SegmentationFault()

	def __ceil__(self) -> None:
		raise SegmentationFault()

	def __gt__(self, other) -> None:
		raise SegmentationFault()

	def __ge__(self, other) -> None:
		raise SegmentationFault()

	def __lt__(self, other) -> None:
		raise SegmentationFault()

	def __le__(self, other) -> None:
		raise SegmentationFault()

	def __eq__(self, other) -> None:
		raise SegmentationFault()

	def __ne__(self, other) -> None:
		raise SegmentationFault()

	def __hash__(self) -> None:
		raise SegmentationFault()

	def __bool__(self) -> None:
		raise SegmentationFault()

	def __nonzero__(self) -> None:
		raise SegmentationFault()

	def __getitem__(self, key) -> None:
		raise SegmentationFault()

	def __setitem__(self, key, value) -> None:
		raise SegmentationFault()

	def __delitem__(self, key) -> None:
		raise SegmentationFault()
	
	def __len__(self) -> None:
		raise SegmentationFault()

	def __contains__(self, item) -> None:
		raise SegmentationFault()

	def __iter__(self) -> None:
		raise SegmentationFault()

	def __next__(self) -> None:
		raise SegmentationFault()

	def __reversed__(self) -> None:
		raise SegmentationFault()

	def __dir__(self) -> None:
		raise SegmentationFault()

	def __format__(self, __format_spec: str) -> str:
		raise SegmentationFault()

	def __matmul__(self, other) -> None:
		raise SegmentationFault()

	def __rmatmul__(self, other) -> None:
		raise SegmentationFault()

	def __imatmul__(self, other) -> None:
		raise SegmentationFault()

	def __truediv__(self, other) -> None:
		raise SegmentationFault()

	def __itruediv__(self, other) -> None:
		raise SegmentationFault()

	def __concat__(self, other) -> None:
		raise SegmentationFault()