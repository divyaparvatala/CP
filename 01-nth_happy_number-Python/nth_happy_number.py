# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

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

def nth_happy_number(n):
	number = 0
	count = 1
	while count < n+1:
		if ishappynumber(number) == True:
			if count==n:
				return number
			else:
				count +=1
				print('hp:',count, number)
				number +=1
			
		else:
			number +=1
			print('not hp', count, number)
	# return number

	# return 0
print(nth_happy_number(3))
# print(ishappynumber(7))