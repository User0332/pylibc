from pylibc.stdlib_h import *

system("echo 'Hello World!'")
system(f"echo {getenv('PATH')}")

abort()