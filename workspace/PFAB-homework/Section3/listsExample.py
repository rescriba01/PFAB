family = ["Annie", "Carla", "Jaime", "Steven", "Lyric", "Jazz", "Soul"]
gpa = [3.45, 3.22, 4.0, 2.77, 3.11]

print family[1]
print family[2]
print gpa[3]

print family[1:3]
print gpa[0:2]

gpa[1] = 4.0

print gpa
del gpa[0]
print gpa

print "Number in family" , len(family)
print "Max value" , max(gpa)

family.sort()
print family
