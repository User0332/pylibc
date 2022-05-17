from pylibc.stdlib_h import *
from pylibc.stdio_h import stdout

system("echo 'Hello World!'")
system(f"echo {getenv('PATH')}")

pyatexit_args(print, "Goodbye World!")
atexit(stdout.flush)

#abort()
exit(1)