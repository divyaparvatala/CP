# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    # pass
    res = [{}]
    for i in range(1,n+1):
        x = {i}
        res.append(x)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if len(res) == k:
                return res
            else:
                if j!=i:
                    y = {i,j}
                    res.append(y)

assert(limitedPowerSet(5,7)==[{}, {1}, {2}, {3}, {4}, {5}, {1, 2}])
assert(limitedPowerSet(6,7)==[{}, {1}, {2}, {3}, {4}, {5}, {6}])
assert(limitedPowerSet(6,10)==[{}, {1}, {2}, {3}, {4}, {5}, {6}, {1, 2}, {1, 3}, {1, 4}])
print('Test cases passed')
