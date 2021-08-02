def isvalidmove(List):
    # print(List)
    if abs(List[0]-List[2]) == abs(List[1]-List[3]):
        # print('----',True)
        return True
    else: 
        # print('qwertyuio')
        return False

def bishopmove(L,count):
    # print(count)
    i2=0
    j2=0
    while count < 7:
        for i in L:
            for j in i:
                if j ==count:
                    j1 = i.index(j)
                    i1 = L.index(i)
            for k in i:
                if k == count+1:
                    # if j == count:
                    j2 = i.index(k)
                    i2 = L.index(i)
        count = count + 1
        # print(i1,i2,j1,j2)
        return [int(i1),int(j1),int(i2),int(j2)]

def bishopvalid(L):
    i = 1
    while i<7:
        if isvalidmove(bishopmove(L,i)) == True:
            i = i+1
            continue
        else:
            return False
    return True


assert(bishopvalid([[1,0,3,0], [0,2,0,4], [7,0,5,0], [0,6,0,0]])==True)
assert(bishopvalid([[1,0,3,0], [0,2,0,4], [0,0,5,0], [7,6,0,0]])==False)
print('Test cases passed')
# print(bishopvalid([[1,0,3,0], [0,2,0,4], [7,0,5,0], [0,6,0,0]]))
# print(bishopvalid([[1,0,3,0], [0,2,0,4], [0,0,5,0], [7,6,0,0]]))