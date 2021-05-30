x=10
y="a"
z=10.5
a=True
print(type(x))
print(type(y))
print(type(z))
print(type(a))

print("My Luck number is : ",x)

import math
print(int(math.sqrt(25)))

# OTP generation

from random import *
for i in range(10):
	print("Your OTP Number is : ",randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')