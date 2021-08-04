# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(n):
    # Your code goes here
    # pass
    if isprime(n)==True:
        if isHappyNumber(n)==True:
            return True
        else:
            return False
    else:
        return False

def isHappyNumber(n):
    if sumOfSquaresOfDigits(n)==1:
        return True
    elif sumOfSquaresOfDigits(n) <10:
        return False
    else:
        return isHappyNumber(sumOfSquaresOfDigits(n))


def isprime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,n,2):
            if n%i==0:
                return False
        return True

def sumOfSquaresOfDigits(n):
    nlist = [(int(i))**2 for i in str(n)]
    return sum(nlist)
        
print(sumOfSquaresOfDigits(13))