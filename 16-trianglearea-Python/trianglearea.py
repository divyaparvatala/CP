# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

def islegaltriangle(s1, s2, s3):
	if s1<=0 or s2<=0 or s3<=0:
		return False
	else:
		if s1+s2<=s3 or s2+s3<=s1 or s3+s1<=s2:
			return False
		elif s1-s2>=s3 or s2-s3>=s1 or s3-s1>=s2:
			return False
		else:
			return True

def trianglearea(s1, s2, s3):
	s = (s1+s2+s3)/2
	if islegaltriangle(s1,s2,s3) == True:
		return ((s)*(s-s1)*(s-s2)*(s-s3))**(1/2)
	else:
		return 0
	# your code goes here
