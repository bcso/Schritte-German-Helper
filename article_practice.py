import random, sys
from pprint import pprint
from const import LWS_10_11, LWS_12_13, LWS_14_15, LWS_8, LWS_9, others

print "Test me on..."
print "1. Food part 1"
print "2. Food part 2"
print "3. Food part 3"
print "4. ALL FOOD"
print "5. House part 1"
print "6. House part 2"
print "7. ALL HOUSE"
print "8. 4 + 7"
print "9. Others"
print "10. 4 + 7 + 9"
choice = raw_input("Enter choice number: ")

if choice == "1":
	items = LWS_8
elif choice == "2":
	items = LWS_9
elif choice == "3":
	items = LWS_10_11
elif choice == "4":
	items = LWS_8 + LWS_9 + LWS_10_11
elif choice == "5":
	items = LWS_12_13
elif choice == "6":
	items = LWS_14_15
elif choice == "7":
	items = LWS_12_13 + LWS_14_15
elif choice == "8":
	items = LWS_8 + LWS_9 + LWS_10_11 + LWS_12_13 + LWS_14_15
elif choice == "9":
    	items = others
elif choice == "10":
    	items = LWS_8 + LWS_9 + LWS_10_11 + LWS_12_13 + LWS_14_15 + others
else:
	print "Input error, please input a number"
	sys.exit()

random.shuffle(items)

a = [x.split()[0] for x in items]
q = [x.split()[1] for x in items]

# Checks guess and answer vectors to see which articles are incorrect. Caluclates score. Reshows the incorrect values for on the spot revision.
# Params
# ---------
# 	guess <str> : string of german articles seperated by a single space, same length as ans
# 	ans <arr> : string array of the correct german articles in order
def c(guess, ans):
	corrections = []
	retest = []
	guess = guess.split()

	# Get the incorrect answers
	for i in xrange(len(ans)):
		if guess[i] != ans[i]:
			corrections.append(i)
	
	if len(corrections) > 0:
		for i in xrange(len(items)):
			if i in corrections:
				print items[i] + " -- !"
				retest.append(items[i])
			else:
				print items[i]
		# Allow users to revise their incorrect answers
		retest = [x.split()[1] for x in retest]
		print "Fill me in again... " + str(retest)

	print str(len(ans)-len(corrections)) + " out of " + str(len(ans)) + " correct!"

allGuess = ""
for i in xrange(len(q)):
	currGuess = raw_input(str(i+1) + "/" + str(len(q)) + " " + q[i] + " : ").lower()
	allGuess = allGuess + " " + currGuess
	if currGuess.strip() == a[i]: 
		print "Correct!"
	else:
		print "Wrong! " + items[i]

raw_input("Press enter to continue.")

c(allGuess,a)

