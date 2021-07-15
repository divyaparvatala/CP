# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.
import pytest

def powerSum(n, k):
    if n<0 or k<0 :
        return 0
    elif n==0 and k==0:
        return 0
    else:
        sum = 0
        for i in range(n+1):
            sum+=(i**k)
            print(sum)
        return sum
    # Your code goes here...
    # return 0

# Write your own test cases here...
@pytest.mark.parametrize('n, k, sum', [
    (0, 0, 0),
    (-1, 1, 0),
    (1, -1, 0),
    (5, 2, 55),
    (3, 5, 276),
])
def test(n,k,sum):
    assert powerSum(n,k) == sum
    # assert powerSum(-1,1) == 0
    # assert powerSum(1,-1) == 0
    # assert powerSum(5,2) == 55


print ("All test cases passed...") 