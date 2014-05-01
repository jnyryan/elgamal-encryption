# elgamal-encryption

I've already looked at other public key encryption methods so now I'll take a look at writing a classic implementation using ElGamaI. Here we'll create the methods required to do the work and borrow some small functions from the crypto libraries, since I already wrote them in a previous post. 

Since ElGamal is based on the Discrete Log problem a little bit of Group Theory is required to understand what is going on, or you can just implement it and see it work.

<linebreak>

### Key Generation methods

First we need to create the Modulus (p), Generator (α), Private Key (x) and Public Key Component (y).

The method ***egKey*** will return a tupple (*p,α,x,y*) that will allow us to create the public key along with it's associated private key.

From this:

- The public key is ***(p, α, y)***- The private key is **x**

```python
"""Generate the keys needed for encryption of size s bites
import random
def egKey(s):
	p = get_safe_prime(s)
	a = get_generator(p)
	x = random.randint(1, p-2)
	y = pow(a,x,p)
	return p, a, x, y
```

The following two methods are utility functions to allow us to calculate the prime and generator

``` python
"""create a safe prime
def get_safe_prime(s):
	safe_prime = 0
	while(True):
		p = num.getPrime(s)
		safe_prime = 2*p+1
		if(num.isPrime(safe_prime)):
			return safe_prime
```

``` python
"""create a generator for the prime from the multiplicitive group defined by the safe prime
def get_generator(safe_prime):
	while(True):
          alpha = random.randint(2, safe_prime-1) 
          if((safe_prime-1)%alpha != 1):
            return alpha
```

## Encryption

The encryption method ***egEnc*** takes the public key components along with a message to be encrypted (m) and returns another tupple *c1,c2*

The cipher text is the pair (**c1, c2**)

```python
"""
def egEnc(p, a, y, m):
	k = random.randint(1, p-2)
	c1 = pow(a,k,p)
	c2 = m * pow(y,k,p)
	return c1, c2
```

## Decryption

The decryption methof ***egDec*** takes the modulus, private key and the cipher text pair and returns the message, *m*.

```python
"""
def egDec(p, x, c1, c2):
	m = (pow(c1, p-1-x)*c2)%p
	return m
```


And that's it you now have a very basic working version of EGamal. It's not very robust and will be slow at very large numbers - but the theory is there.
