from sys import argv

script, input_file = argv

code = None

def CheckSum2020(a,b,c):
	if a + b +c == 2020:
		code = a*b*c
		#print("The answer has been found! ",a," and ",b," equal 2020!\n")
		#print("Multiplying those together is ",code)
		return code
	else:
		#print("Result Failed: ",a," + ", b," does not equal 2020.")
		return None

data = []

with open(input_file) as csvfile:
	data = [float(s) for line in csvfile.readlines() for s in line[:-1].split(' ')]

for i in data:
	if code != None:
		break
	for j in data:
		if code != None:
			break
		for k in data:
			code = CheckSum2020(i,j,k)
			if code != None:
				print("The magic code is: ",code, "using ",i," ",j," and ",k)
				break


 
