from sys import argv
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 

passports = contents.split("\n\n") # Split on blank lines only
passports = [i.replace('\n', ' ') for i in passports] # Clean up stray \n's in the dataset

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"] # Passport fields 
fieldID = 0
# for each element, count the number of required fields 
numFields = 0
passportData = []
validPassports = 0
northpolepassports = 0

for i in passports:
	split = i.split()
	print(split)
	dataLoc = 0
	hasCID = False	
	numFields = 0
	for j in split:
		byrLoc = j.find('byr')
		if byrLoc != -1:
			byrVal = j[4:]
			numFields += 1
			print("Found! Value is: ",byrVal, "Current valid fields: ",numFields)
		iyrLoc = j.find('iyr')
		if iyrLoc != -1:
			iyrVal = j[4:]
			numFields += 1
			print("Found! Value is: ",iyrVal, "Current valid fields: ",numFields)
		eyrLoc = j.find('eyr')
		if eyrLoc != -1:
			eyrVal = j[4:]
			numFields += 1
			print("Found! Value is: ",eyrVal, "Current valid fields: ",numFields)
		hgtLoc = j.find('hgt')
		if hgtLoc != -1:
			hgtVal = j[4:]
			numFields += 1
			print("Found! Value is: ",hgtVal, "Current valid fields: ",numFields)
		hclLoc = j.find('hcl')
		if hclLoc != -1:
			hclVal = j[4:]
			numFields += 1
			print("Found! Value is: ",hclVal, "Current valid fields: ",numFields)
		eclLoc = j.find('ecl')
		if eclLoc != -1:
			eclVal = j[4:]
			numFields += 1
			print("Found! Value is: ",eclVal, "Current valid fields: ",numFields)
		pidLoc = j.find('pid')
		if pidLoc != -1:
			pidVal = j[4:]
			numFields += 1
			print("Found! Value is: ",pidVal, "Current valid fields: ",numFields)
		cidLoc = j.find('cid')
		if cidLoc != -1:
			cidVal = j[4:]
			numFields += 1
			hasCID = True
			print("Found! Value is: ",cidVal, "Current valid fields: ",numFields)
	print("Valid Fields: ",numFields)
	print("Has CID?",hasCID)
	if numFields == len(fields):
		validPassports += 1
		print("We have a valid passport here!","\n")
	elif (numFields == 7) and (hasCID == False):
		validPassports += 1
		northpolepassports += 1
		print("We have a valid* passport here!", northpolepassports,"\n")
		
print("Total number of valid passports: ", validPassports)
print("Total number of North Pole Passports: ", northpolepassports)




