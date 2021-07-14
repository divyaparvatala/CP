# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	textlist = [i for i in text]
	res = []
	for i in textlist:
		if i not in res:
			res.append(i)
	resstr = ''
	for i in res:
		resstr+=i
	return resstr

print(removeduplicate('JavaPython'))