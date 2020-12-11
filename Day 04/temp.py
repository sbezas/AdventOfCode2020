from sys import argv
import string
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 

passports = contents.split("\n\n") # Split on blank lines only
passports = [i.replace('\n', ' ') for i in passports] # Clean up 
#print(passports[0])
split = passports[1].split()
print(split)
hclVal = split[6]
hclVal = hclVal[4:]
print(hclVal)
#if (hgtVal[-2:] == "in") and (59 <= int(hgtVal[-6:-3]) <= 76):

'''
if len(hclVal[4:]) != 7:
	print("No good")
else:
	print("All good")
	for i in hclVal[5:]:
		if (i not in string.ascii_letters[0:6]) and (i.isnumeric() == False) :
			print("Fail Letters and numbers")
		else:
			print("Pass Letters and numbers")'''
#print(string.ascii_letters[0:6])
if len(hclVal) != 7:
	print("No good")
else:
	print("All good")
	for i in hclVal[1:]:
		if (i not in string.ascii_letters[0:6]) and (i.isnumeric() == False) :
			print("Fail Letters and numbers")
		else:
			print("Pass Letters and numbers")
