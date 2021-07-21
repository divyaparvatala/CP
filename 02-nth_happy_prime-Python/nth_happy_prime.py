# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
	if n%2 ==0:
		return False
	for i in range(3,n,2):
		if n%i==0:
			return False
		else:
			return True


def ishappynumber(n):
    # your code goes here
	if n<=0:
		return False
	else:
		count = 0
		# while count<10:
		while n > 1:
			nlist = [int(i) for i in str(n)]
			n=0
			for i in nlist:
				n += i**2
				count +=1
				if count ==100:
					return False
		return True

def fun_nth_happy_prime(n):
	number = 0
	count = 0

	while count < n+1:
		if ishappynumber(number) == True and isPrime(number) == True:
			if count==n:
				return number
			else:
				count +=1
				print('hp:',count, number)
				number +=1
			
		else:
			number +=1

print(fun_nth_happy_prime(5))