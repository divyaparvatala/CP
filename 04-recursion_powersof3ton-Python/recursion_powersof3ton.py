# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	if n<1:
		return None
	else:
		power = 0
		L=[]
		return powerof3ton(n,power,L)

	# pass

def powerof3ton(n,power,L):	
	if 3**power<=n:		
		print(L,power)
		L.append(3**power)
		return powerof3ton(n,power+1,L)
	else:
		return L

print(recursion_powersof3ton(4))