from sys import argv
import string
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 

groupresponses = contents.split("\n\n")
letters = string.ascii_letters[0:26]

def countUnique(groupList):
	group_set = set(groupList)
	n = len(group_set)
	return n

def countAlphabet(a):
	print("a")

totalYes = 0

for k in groupresponses:
	split = k.split()
	print(split)
	for i in letters:
		countAlpha = 0
		for j in split:
			countAlpha += j.count(i)
#			print("Count of ",i,"is ",countAlpha)
		if countAlpha == len(split):
			totalYes += 1

print("Total yes to track: ",totalYes)
	
