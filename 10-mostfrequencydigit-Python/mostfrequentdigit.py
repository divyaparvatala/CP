# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	nlist = [int(i) for i in str(n)]
	print(nlist)
	freq = nlist.count(nlist[0])
	digit = 0
	equallist=[]
	for i in nlist:
		# print(i)
		freq_ = nlist.count(i)
		print('first',i,freq_,freq)
		if freq_>freq:
			freq = freq_
			# digit = i
			equallist.clear()
			equallist.append(i)
			print('second',i,freq_,freq)
		elif freq_==freq:
			equallist.append(i)
			# digit = min(i,freq_)
			# print('digit',digit)
	return min(equallist)


print(mostfrequentdigit(5231123123123))



	# your code goes here
	# pass