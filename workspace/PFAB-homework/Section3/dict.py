gpas = {'Smith' : 3.25 , 'Johnson' : 3.22 , 'Thompson' : 2.55 , 'Themes' : 1.7 , 'Morgan' : 3.92 }

print gpas['Smith']
print gpas['Morgan']

newGPA = input("What is the new GPA for Smith?")

gpas['Smith'] = newGPA

print "Smiths GPA is " , gpas['Smith']
print gpas

del gpas['Themes']
print gpas

print len(gpas)

if gpas.has_key('Johnson'):
	print "Johnson is in the dictionary"

