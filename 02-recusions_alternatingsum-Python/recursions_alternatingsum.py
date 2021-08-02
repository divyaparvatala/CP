# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	if len(l)==0:
		return 0
	elif len(l)==1:
		# print('length :   ', len(l))
		# print(l)
		return l[0]
	else:
		# if len(l)%2==0:
		# # 	print('list: ',l[1:])
		# # 	print('first element :', l[0])
		# # 	print('length :   ', len(l))
		# 	return l[0] - fun_recursions_alternatingsum(l[1:])
		# elif len(l)%2==1:
		# # 	print('list: ',l[1:])
		# # 	print('first element :', l[0])
		# # 	print('length :   ', len(l))
		print('0, [1:], [2:]',l[0], fun_recursions_alternatingsum(l[1:]), fun_recursions_alternatingsum(l[2:]))
		print('res',l[0] - fun_recursions_alternatingsum(l[1:]) + fun_recursions_alternatingsum(l[2:]))
		return fun_recursions_alternatingsum(l[:2]) - fun_recursions_alternatingsum(l[:2])
print(fun_recursions_alternatingsum([1,2,3,4]))