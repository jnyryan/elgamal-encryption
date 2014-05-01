#!/usr/bin/env python
# encoding:UTF-8
"""

Implement ElGamal using the following routines: 

	(Integer, Integer, Integer, Integer) egKey(Integer) 
	(Integer, Integer) egEnc(Integer, Integer, Integer, Integer) 
	Integer egDec(Integer, Integer, Integer, Integer)

such that:
 egKey(s) will return a tuple (p,α,x,y) where p is a safe prime, α a generator, and x and y are the public and private components of the ElGamal key.
 egEnc(p, α, y, m) will return (c1, c2)
 egDec(p, x, c1, c2) will return m

"""
import p3_pair
import random

def egKey(s):
	p,a = p3_pair.pair(s)
	x = random.randint(1, p-2)
	y = pow(a,x,p)
	return p, a, x, y

def egEnc(p, a, y, m):
	k = random.randint(1, p-2)
	c1 = pow(a,k,p)
	c2 = m * pow(y,k,p)
	return c1, c2

def egDec(p, x, c1, c2):
	m = (pow(c1, p-1-x)*c2)%p
	return m

#####################################################################
# Tests

if __name__ == "__main__":
	
	message = 12345678
	print "Message: ", message
	p,a,x,y = egKey(24)
	print p,a,x,y
	c1, c2 = egEnc(p, a, y, message)
	message = egDec(p, x, c1, c2)
	print "Decrypted: " ,  message

