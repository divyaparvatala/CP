# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	centre_dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
	radius_dist = r1+r2
	if centre_dist<=radius_dist:
		return True
	else:
	# your code goes here
		return False 
