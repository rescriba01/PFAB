Bradys = ["Mike" , "Carol" , "Marsha" , "Jan" , "Cindy" , "Greg" , "Peter" , "Bobby" , "Alice"]

print len(Bradys)

numBradys = 9
counter = 0

while counter < numBradys:
	print Bradys[counter]
	counter = counter + 1
#Sorted 

Bradys.sort()
print Bradys

#For Loop

x = len(Bradys)
for x in Bradys:
	print x
