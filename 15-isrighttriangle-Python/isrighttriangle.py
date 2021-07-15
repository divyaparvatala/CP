# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	m1 = (y2-y1)/(x2-x1)
	m2 = (y3-y2)/(x3-x2)
	m3 = (y1-y3)/(x1-x3)
	if m1*m2==-1 or m2*m3==-1 or m3*m1==-1:
		return True
	else:
		return False
	# pass
