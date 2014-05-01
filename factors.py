#!/usr/bin/env python
"""

 Implement the following routine: 

 	Integer* factors(Integer)

such that factors(x) will return a list of integer values that are 
the factors of x. 

Note that if a prime p has a power e > 0 in the factorization of x, 
then p should appear e times in the result.

"""

def factors(x):
	factors = []
	counter = 2
	while x > 1:
		if x % counter == 0:
			factors.append(counter)
			x = x / counter
		else:
			counter = counter + 1
	return factors

#####################################################################
# Tests

if __name__ == "__main__":
	print "Practical 6 - Factors"
	#over 300 digit long integers
	longint1 = 355555**62
	longint2 = 429024**70

	print factors(12)
	print factors(20)
	print factors(600)
	print factors(4123456789)
	print factors(longint1)
	print factors(longint2)
	print "Done."