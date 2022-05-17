from pylibc.stdlib_h import (
	cstrtol as strtol,
	malloc,
	free,
	atoi,
	atol,
	atof
)


endptr = malloc(1)

print(strtol("-123", endptr, 10))

print(*endptr)

print(strtol("12&", endptr, 10))

print(*endptr)

print(atoi("100"), atol("100"), atof("100"))

free(endptr)

print(*endptr)