# Implementation of the Tonelli-Shanks algoritm as described at:
# https://en.wikipedia.org/wiki/Tonelli%E2%80%93Shanks_algorithm

 
# Determines if n is a quadratic residue of an 
# odd prime p by using Euler's criterion.
def is_quadratic_residue(n, p):
	if n % p == 0:
		return True
	return pow(n, (p - 1)//2, p) == 1
	

# Given an odd prime p and an integer n
# This is an algorithm to find a mod-p square root of n when possible
# Can delete all the print statements once its working.
def tonelli_shanks(p, n):
	# Case when p|n, so n=0(mod p). The square root of 0 is 0. 
	if n % p == 0:
		return 0

	# So we can assume n is coprime to p, i.e. p does not divide n.
	# Use Euler's criteria to see if a solution exists or not
	if not is_quadratic_residue(n, p):
		print("This value of n is not a quadratic residue.")
		return None
	else:
		print("This value of n is a quadratic residue.")

	# If p=3(mod 4) and we know n is a quadratic residue then 
	# we can solve x^2=n(mod p) directly
	if p % 4 == 3:
		return pow(n, (p + 1)//4, p)
	
	# So now p=1(mod 4), (although this is not needed in the algorithm).
	# Write p - 1 = (2^S)(Q) where Q is odd
	Q = p - 1
	S = 0
	while Q % 2 == 0:
		S += 1
		Q //= 2
	print("Q=", Q)
	print("S=", S)

	# Find a quadratic non-residue of p by brute force search
	z = 2
	while is_quadratic_residue(z, p):
		z += 1
	print("z=", z)

	# Initialize variables
	M = S
	c = pow(z, Q, p)
	t = pow(n, Q, p)
	R = pow(n, (Q + 1)//2, p)

	print("M=", M)
	print("c=", c)
	print("t=", t)
	print("R=", R)
	
	while t != 1:
		print("LOOP")

		# Calculate i
		i = 0
		temp = t 
		while temp != 1:
			i += 1
			temp = (temp * temp) % p
		print("i=", i)
		
		# Calculate b, M, c, t, R
		pow2 = 2 ** (M - i - 1)
		b = pow(c, pow2, p)
		M = i
		c = (b * b) % p
		t = (t * b * b) % p
		R = (R * b) % p
		print("b=", b)
		print("M=", M)
		print("c=", c)
		print("t=", t)
		print("R=", R)

	# We have found a square root
	return R


# Given an elliptic curve specified by p, a, b and given an
# x-value this function calculates when possible a corresponding 
# y-value such that (x,y) is on the elliptic curve.
def get_y_value_elliptic_curve(p, a, b, x):
	n = (x * x * x + a * x + b) % p
	# Applying Tonelli-Shanks to get the square root of n 
	# (if it exists) will give us the y-value for one of the
	# desired point on the elliptic curve.
	return tonelli_shanks(p, n)

	


# The Elliptic Curve P-224
p = 26959946667150639794667015087019630673557916260026308143510066298881 
a = -3
b = int('b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4', 16)

# Make up a random number x and calculate y (if it exists)
x = 2021
y = get_y_value_elliptic_curve(p, a, b, x)
if y == None: 
	exit()
print("y=", y, "\n")

# check that point is indeed on the elliptic curve
if (y * y - (x * x * x + a * x + b)) % p == 0:
	print("(", x, ",", y, ")")
	print("Point has been verified to be on the elliptic curve!")


