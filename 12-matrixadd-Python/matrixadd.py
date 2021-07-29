# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.


def ismatrix(X):
	rows = len(X)
	cols = len(X[0])
	# print(rows,cols)
	if rows == 1 and cols == 1:
		return True
	else:
		for i in range(rows-1):
			# print('---')
			if len(X[i])==len(X[i+1]):
				return True
			else:
				return False

def matrixadd(L, M):
	if ismatrix(L) != True or ismatrix(M) != True:
		return None
	else:
		lrows = len(L)
		lcols = len(L[0])
		mrows = len(M)
		mcols = len(M[0])
		M2 = M
		N = M2
		if lrows == mrows and lcols == mcols:
			for i in range(lrows):
				for j in range(lcols):
					print('i,j: ',i,j)
					print('bef  ',N[i][j])
					N[i][j] = L[i][j]+M[i][j]
					print('aft  ',N[i][j])
					print(N)
			return N

print(matrixadd([[1,  2,  3],[4,  5,  6]], [[21, 22], [24, 25, 26]]))