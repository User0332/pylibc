from pylibc.stdlib_h import malloc
from pylibc.stdio_h import (
	getchar, 
	putchar, 
	printf, 
	puts, 
	cscanf as scanf
)

someint = malloc(1)
mystr = "hi"
buff = malloc(20)

puts("Enter some input: ")
scanf("%20s", buff)
puts("Enter an integer: ")
scanf("%d", someint)
putchar(getchar())
putchar('\n')
printf("integer input:%i\nmystr:%s\ninput buffer:%s\nsome character:%c", *someint, mystr, buff, 100)