from pylibc.stdlib_h import cstrtol as strtol


endptr = []

print(strtol("-123", endptr, 10))

print(*endptr)

print(strtol("12&", endptr, 10))

print(*endptr)