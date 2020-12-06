from sys import argv
script, input_file = argv

passwordlist = []
validcount = 0
i=0
with open(input_file, "r") as f:
	passwordlist = [current_place.rstrip() for current_place in f.readlines()]

for i in passwordlist:	
	#Locate positions
	## Minimum value position
	if i[1] == "-":
		MinEndPos = 0
		MinLength = 1
		MinVal = int(i[0])
	else:
		MinEndPos = 1
		MinLength = 2
		MinVal = int(i[0:MinEndPos+1])
	
		
	## Maximum value position
	MaxStartPos = MinEndPos + 2
	if i[MaxStartPos+1] == " ":
		MaxEndPos = MaxStartPos
		MaxLength = 1
		MaxVal = int(i[MaxStartPos])
	else:
		MaxEndPos = MaxStartPos + 1
		MaxLength = 2
		MaxVal = int(i[MaxStartPos:MaxEndPos+1])
		
	# Identify check letter
	checkletter = i[MaxEndPos+2]
	
	# Identify password
	passwordStartPos = MaxEndPos + 3
	password = i[passwordStartPos:]
	
	# Count number of checkletters in password
	CheckLetterCount = int(password.count(checkletter))
	
	# Determine if valid
	if MinVal <= CheckLetterCount <= MaxVal:
		print("Valid Password!")
		validcount += 1	
	else:
		print("INVALID PASSWORD!")
				
	#Output
	print("Current password: ",i)
	print("Length:",len(i))
	print("MinEndPos: ",MinEndPos)
	print("MinLength: ",MinLength)
	print("MaxStartPos: ",MaxStartPos)
	print("MaxEndPos: ",MaxEndPos)
	print("MaxLength: ",MaxLength)
	print("MinVal: ",MinVal)
	print("MaxVal: ",MaxVal)
	print("Check letter: ", checkletter)
	print("Password: ", password)
	print("Number of Check letters:" ,CheckLetterCount)
	print("Valid passwords: ",validcount)
	print("END OF RUN")
	print("\n")


