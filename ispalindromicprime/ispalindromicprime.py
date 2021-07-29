def isprime(n):
    if n ==2:
        return True
    else:
        if n%2 == 0:
            return False
        else:
            for i in range(3,n,2):
                if n%i == 0:
                    return False
            return True
    # return 0

def isPalindromic(n):
    nlist = [int(i) for i in str(n)]
    for i in range(len(nlist)):
        if nlist[i] == nlist[-i]:
            return True
    # return 0

def isPalindromicPrime(n):
    if isprime(n) == True and isPalindromic(n) == True:
        return True
    else:
        return False
    # return 0

# print(isPalindromic(12121))


assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")