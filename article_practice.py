import random, sys
from pprint import pprint

# Page 8 LWS
LWS_8 = ['das Broetchen',
'das Brot',
'das Ei',
'das Mehl',
'das Wuerstchen',
'der Apfel',
'der Euro',
'der Hunger',
'der Joghurt',
'der Kafee',
'der Kuchen',
'der Saft',
'der Zucker',
'die Banane',
'die Birne',
'die Butter',
'die Kartoffel',
'die Milch',
'die Orange',
'die Pfannkuchen',
'die Schokolade',
'die Tomate',
'die Welt',
'die Zwiebel']

# Page 9 LWS
LWS_9 = ['das Bier',
'das Fleisch',
'das Gemuese',
'das Gramm',
'das Hackfleisch',
'das Kilo',
'das Lebensmeittel',
'das Mineralwasser',
'das Obst',
'das Oel',
'das Pfund',
'das Regal',
'das Salz',
'das Sonderangebot',
'das Wasser',
'der Cent',
'der Fisch',
'der Kaese',
'der Liter',
'der Preis',
'der Prospeckt',
'der Reis',
'der Tee',
'der Wein',
'die Abteilung',
'die Wurst']

# Page 10-11 LWS
LWS_10_11 = ['das Cola',
'das Essen',
'das Getraenk',
'das Glas',
'das Haehnchen',
'das Restaurant',
'das Rezept',
'das Steak',
'der Durst',
'der Pfeffer',
'der Salat',
'der Tag',
'die Dose',
'die Flasche',
'die Mensa',
'die Pizza',
'die PommesFrites',
'die Portion',
'die Sahne',
'die Sosse',
'die Suppe']

LWS_12_13 = ["die Wohnung",
"die Lampe",
"das Zimmer",
"die Kueche",
"das Bad",
"der Flur",
"die Toilette",
"der Balkon",
"das Wohnzimmer",
"das Haus",
"der Monat",
"das Beispiel",
"der Schrank",
"der Kuehlschrank",
"das Sofa",
"der Tisch",
"der Stuhl",
"der Fernseher",
"die Dusche",
"der Herd",
"die Badewanne",
"der Teppich",
"der Sessel",
"die Moebel",
"das Geraet",
"die Farbe",
"der Zentimeter",
"das Handy"]

LWS_14_15 = ["die Arbeit",
"die Anzeige",
"das Ehepaar",
"der Garten",
"das Apartment",
"der Raum",
"der Stock",
"der Anruf",
"das TV",
"die Garage",
"der Quadrameter",
"die Miete",
"das Buch",
"der Stift",
"der Schreibtisch",
"das Holz",
"der Meter",
"der Platz",
"der Computer",
"das Heft"]

others = ["die Dozentin",
"die Vorlesung",
"der Name",
"das Papier",
"der Buchstabe",
"der Satz",
"das Wort",
"das Gespraech",
"das Handy",
"der Kochkurs",
"der Rotwein",
"die Traube",
"das Geld",
"die Melone",
"die Tuete",
"die Zeit",
"das Problem",
"das Buecherregal",
"das Picknick"
]

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

guess = ""
for i in xrange(len(q)):
	guess = guess + " " + raw_input(str(i+1) + "/" + str(len(q)) + " " + q[i] + " : ").lower()

raw_input("Press enter to continue.")

c(guess,a)

