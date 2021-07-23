def additive(n):
    sum_ = 0
    nlist = [int(i) for i in str(n)]
    sum_ = sum(nlist)
    return sum_



def isprime(n):
    if n == 2:
        return True
    elif n%2 ==0:
        return False
    else:
        for i in range(3,n,2):
            if n%i ==0:
                return False
    return True

def isAdditivePrime(n):
    if isprime(n) == True:
        if isprime(additive(n))==True:
            return True
    # if additive(n)
    return False

# print('ap',isAdditivePrime(13))
# print('ip',isprime(13))

assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")