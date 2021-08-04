# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	count = -1
	num = 0
	while count<n:
		num+=1
		if property309(num) == True:
			count+=1
			# num+=1
		else:
			# num+=1
			continue
	# Your code goes here
	return num


def property309(n):
	string = "0123456789"
	prop = str(n**5)
	for i in string:
		if i not in prop:
			return False
	return True

# print(property309(309))
print(nthwithproperty309(0))
# print(307**5)