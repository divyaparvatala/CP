def create0matrix(n):
    nlist = []
    for i in range(n):
        nlist.append([0]*n)
        
        # for j in range(n):
            # l.append(0)
    # for i in n2dlist[]
    return nlist

def create2dlist(n):
    matrix = create0matrix(n)
    # print('matrix',matrix)
    matrix[0] = [x+1 for x in matrix[0]]
    for i in range(0,len(matrix)):
        matrix[i][0] = 1
    print(matrix)
    for i in range(1,len(matrix)):        
        for j in range(1,len(matrix)):
            print(matrix[i-1][j], matrix[i][j-1])
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix            


print(create2dlist(5))