# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def fun_kaprekarnumber(n):
    m = n**2
    length = len(str(m))
    if length%2==0:
        m1 = m//(10**(length/2))
        while m1%10==0:
            m1=m1/10
        m2 = m%(10**(length/2))
    else:
        m1 = m//(10**((length+1)/2))
        print(m1)
        if m1!=0:
            while m1%10==0:
                m1=m1/10
        # print('length, m1, length/2', length, m1, (length+1)/2)
        m2 = m%(10**((length+1)/2))
        # print('length, m2, length/2', length, m2, (length+1)/2)
    # print(m,m1,m2)
    if int(m1+m2) == n:
        # print(n,m1,m2,int(m1+m2))
        return True
    else:
        # print(n,m1,m2,int(m1+m2))
        return False

def fun_nth_kaprekarnumber(n):
    count = -1
    num = 1
    while count<n:
        if fun_kaprekarnumber(num)==True:
            if count == n:
                return num-1
            else:
                count+=1
                num+=1
        else:
            # if count
            num+=1
            continue
            
    return num-1


print(fun_kaprekarnumber(45))
# print(fun_nth_kaprekarnumber(10))