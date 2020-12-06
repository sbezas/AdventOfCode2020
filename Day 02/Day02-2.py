from sys import argv
script, input_file = argv

passwordlist = []
validcount = 0
i=0
with open(input_file, "r") as f:
	passwordlist = [current_place.rstrip() for current_place in f.readlines()]

for i in passwordlist:
	split = i.split()
	range = split[0].split('-')
	firstPos = int(range[0])
	secondPos = int(range[1])
	letter = split[1][0]
	password = split[2]
	
	check = password[firstPos-1].count(letter) + password[secondPos-1].count(letter)
	if check == 1:
		validcount += 1
		print(i," is Valid!")
	else:
		print(i," is invalid!")
	
print(validcount)
