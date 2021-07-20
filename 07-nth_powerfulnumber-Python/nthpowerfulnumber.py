# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def factorlist(x):
	factlist=[]
	for i in range(1,x+1):
		if x%i==0:
			factlist.append(i)
	return factlist

def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			return False        
	return True

def ispowerfulnumber(x):
	factlist = factorlist(x)
	print('factlist: ',factlist)
	for i in factlist:
		if isprime(i)==True:
			print('i and i**2',i,i**2)
			if i**2 not in factlist:
				print('i**2 not in factlist')
				return False
	print('i**2 in factlist')
	return True

def nthpowerfulnumber(n):
	number=1
	count = 0
	while count<n+1:
		print('number= ',number)
		if ispowerfulnumber(number) == True:
			count+=1
			number+=1
		else:
			number+=1	
	return number-1

# print(nthpowerfulnumber(10))
# print(ispowerfulnumber(64))