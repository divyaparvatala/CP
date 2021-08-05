# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(L):
    # Your code goes here...
    M = []
    for row in L :
        M = [[L[j][i] for j in range(len(L))] for i in range(len(L[0]))]

    
    for i in L:
        for j in i:
            # if j>len(i):
                # return False
            if i.count(j)>1:
                return False

    for i in M:
        for j in i:
            # if j>len(i):
            #     return False
            if i.count(j)>1:
                return False
    return True

    # pass

assert(isLatinSquare([[1, 2, 3], [2, 3, 1], [3, 1, 2]])==True)
assert(isLatinSquare([[1, 2, 1], [2, 3, 1], [3, 1, 1]])==False)
assert(isLatinSquare([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2],[4, 1, 2, 3]])==True)
print('Test cases passed')