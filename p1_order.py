#!/usr/bin/env python
# encoding:UTF-8
"""

Implement the following routine: 

	Integer order(Integer, Integer∗, Integer)

such that order(p,f,a) will return the order of a in the 
group Z∗p where f is a list of the prime factors of p − 1. 
Ensure that your method works when f contains duplicates. 
For example, consider cases where p = 17.

Solution
– Start by setting t equal to p−1,i.e.,t=p1 p2...pn. – For each prime factor pi, do the following:
1. Test if a t′ ≡1(modp)
	where t′ =t/pi.
2. If this is true, then pi must not be a prime factor of t; so set t to equal t′. 
3. If this is false, then pi is a prime factor; so do not change t.

"""

def order(p,factors,a):
	t = p-1
	for f in factors:
		tt = t/f
		print "tt:", tt
		if(p%(a**tt)==1):
			t = tt
	return t

#####################################################################
# Tests

import Crypto.Util.number as CUN
import factors as FAC
if __name__ == "__main__":
	
	p = 17 #CUN.getPrime(20)
	f = FAC.factors(p-1)
	a = 4
	print p, f, a
	print order(p,f,a)

