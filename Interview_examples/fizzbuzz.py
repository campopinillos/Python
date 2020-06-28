#!/usr/bin/env python3
lis = [0 if x == 0 else "FizzBuzz" if (x % 5 == 0 and x % 3 == 0) else 
	   "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in range(51)]
print(lis)
