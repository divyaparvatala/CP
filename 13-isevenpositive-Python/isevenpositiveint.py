# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isNumeric(x):
	res = x.isnumeric()
	return res

def isevenpositiveint(x):
	if isNumeric(str(x)) == True:
		if int(x)%2 ==0:
			return True
		else:
			return False
	else:
		return False
	# your code goes here
	# pass
