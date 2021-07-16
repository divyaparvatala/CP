# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 
import math

def factorial(n):
	product = 1

	for i in range(1,n+1):
		product=product*i
		# print(product)
	return product


def nCk(n,k):
	nfactorial = factorial(n)
	kfatorial = factorial(k)
	nmkfactorial = factorial(n-k)


	# nfactorial = math.factorial(n)
	# kfatorial = math.factorial(k)
	# nmkfactorial = math.factorial(n-k)
	return nfactorial/(kfatorial*nmkfactorial)


def fun_pascaltrianglevalue(row, col):
	if row>= 0 and col>=0:
		if col<=row:
			val = nCk(row,col)
			return val
		else:
			return 0
