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

def ispalindrome(n):
    nlist = [int(i) for i in str(n)]
    nlistopp = nlist[::]
    for i in range(len(nlist)):
        if nlist[i]==nlistopp[i]:
            return True


def isPalindromicPrime(n):
    if isprime(n) == True and ispalindrome(n)== True:
        return True

    else:
        return False





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