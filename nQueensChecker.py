# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on 
# an NxN chessboard such that no two queens are attacking each other. 
# For most values of N, there are many ways to solve this problem. 
# Here, you will write the function nQueensChecker(board) 
# that takes a 2d list of booleans where True indicates 
# a queen is present and False indicates a blank cell, 
# and returns True if this NxN board contains N queens 
# all of which do not attack any others, and False otherwise.

def nQueensChecker(a):
    # Your code goes here...
    # pass
    li = []
    lj = []
    # l=[]
    for i in a:
        for j in i:
            if j == True:
                li.append(a.index(i))
                lj.append(i.index(j))

    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                if li[i]-li[j] == lj[i]-lj[j]:
                    print(i,j)
                    return False
            if len(li) != len(set(li)):
                return False 
            elif len(lj) != len(set(lj)):
                return False
    return True
            
    # return li,lj

assert(nQueensChecker([
   [0, 0, 0, 1, 0],
   [0, 1, 0, 0, 0],
   [0, 0, 0, 0, 1],
   [0, 0, 1, 0, 0],
   [1, 0, 0, 0, 0]
])==True)

assert(nQueensChecker([
   [0, 0, 0, 1, 0],
   [0, 1, 0, 0, 0],
   [0, 0, 0, 0, 1],
   [0, 0, 0, 1, 0],
   [1, 0, 0, 0, 0]
])==False)

print('testcases passed')