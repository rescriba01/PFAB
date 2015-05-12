subject = ("English", "Algebra", "Biology", "Music", "Physical Education", "Social Studies")

#print subject[0]
#print subject[3]

#subject[3] = "Psychology" Tuple is immutable-- Can't be changed once created

x = len(subject)
counter = 0

#while counter < x:
#	print subject[counter]
#	counter = counter + 1

for x in subject:
	print x

