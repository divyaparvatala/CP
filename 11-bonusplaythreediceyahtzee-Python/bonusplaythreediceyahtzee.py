# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
	# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
	# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
	# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 



# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
2345	413	
23 	445
443		



def firstroll(dice):
	return dice%1000

# 2345413 => 413

def score(roll):
	d0 = roll%10
	d1 = (roll//10)%10
	d2 = roll//100
	if d0==d1==d2:
		return 20 + (d0*3)
	elif d0==d1 and d1!=d2:
		return 10 + (d1*2)
	elif d1==d2 and d2!=d0:
		return 10 + (d2*2)
	elif d2==d0 and d0!=d1:
		return 10 + (d0*2)
	elif d0!=d1 and d1!=d2 and d2!=d0:
		return max(d0,d1,d2)

# 413->4

def bonusplaythreediceyahtzee(dice):

# 2345413 => 413 => 0rep => 4 and 3rd and 4th 
	dicelist = [int(i) for i in str(dice)]
	# [2,3,4,5,4,1,3]
	roll1 = firstroll(dice)	
	# 413
	listroll1 = [int(i) for i in str(roll1)]
	# [4,1,3]
	if listroll1[0]==listroll1[1] and listroll1[1]==listroll1[2]:
		return roll1, score(roll1)
		# 555 => 555,20+15
	elif listroll1[0]==listroll1[1] and listroll1[1]!=listroll1[2]:
		# 2345336 	336		335		334
		# 336 => 33 and [3]
		listroll1.remove(listroll1[2])
		listroll1.append(listroll1[3])
		listroll1.pop()
		# 335
		if listroll1[0]==listroll1[1] and listroll1[1]==listroll1[2]:
			return roll1, score(roll1)
		elif listroll1[0]==listroll1[1] and listroll1[1]!=listroll1[2]:
			listroll1.remove(listroll1[2])
			listroll1.append(listroll1[3])
			listroll1.pop()
			return


	if d0==d1  and d1==d2:
		return roll1, score(roll1)
	# Your code goes here
	elif d0==d1 and d1!=d2:
		

	pass
