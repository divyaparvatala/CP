# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
	res =[]
	for i in L:
		if len(res)<=k:
			res.append(i)
		else:
			count=-1
			print(res)
			while count>-k:
			# for j in range(-(k),-1):
				if i == res[count]:
					print(i,count)
					count-=1
					
				else:
					# print(i,j)
					res.append(i)
					# count-=1
			# print(res)
					break	

	print(res)
	return res

print(shortenlongruns([2, 3, 5, 5, 5, 3], 3))
