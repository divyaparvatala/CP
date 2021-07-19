# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


# def fun_applycaesarcipher(msg, shift):
# 	lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 	upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# 	msglist = [i for i in msg]
# 	shiftmsglist = []
# 	shiftmsg = ''
# 	for i in msg:
# 		if i in lower:
# 			print(i)
# 			i = lower[(lower.index(i)+shift)%26]
# 			print(i)
# 			shiftmsglist.append(i)
# 		elif i in upper:
# 			print(i)
# 			i = upper[(upper.index(i)+shift)%26]
# 			print(i)
# 			shiftmsglist.append(i)
# 		else:
# 			print(i)
# 			shiftmsglist.append(i)

# 	return "".join(shiftmsglist)
# print(fun_applycaesarcipher("We Attack", 1))

def fun_applycaesarcipher(msg, shift):
	msglist = [i for i in msg]
	# print(msglist)
	ordlist = [ord(i) for i in msg]
	shiftmsg = ''
	newilist = []
	newi = 0
	for i in msglist:
		if i.isalpha():
			if i.isupper():
				newi = ((ord(i)+shift-65)%26)+ 65
				print(ord(i),newi)
				newilist.append(chr(newi))
			elif i.islower():
				newi = ((ord(i)+shift-97)%26) + 97
				print(ord(i),newi)
				newilist.append(chr(newi))
		else:
			newilist.append(i)
	
	return "".join(newilist)
	
print(fun_applycaesarcipher("We Attack", 1))







