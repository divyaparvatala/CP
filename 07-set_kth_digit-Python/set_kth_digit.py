# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

#n=12345	k=2		d=9		ans=12945

def fun_set_kth_digit(n, k, d):
	m=n
	n=abs(n)
	x = n//(10**(k+1))
	y = d*(10**k)
	z = n%(10**k)
	if m<0:
		return (x*(10**(k+1))+y+z)*(-1)
	else:
		return x*(10**(k+1))+y+z




		# return n
# print(fun_set_kth_digit(468,0,1))
