from sys import argv
import csv

script, input_file = argv

code = 0
a = 0
b = 0

def CheckSum2020(a,b):
	if a + b == 2020:
		code = a*b
		#print("The answer has been found! ",a," and ",b," equal 2020!\n")
		#print("Multiplying those together is ",code)
		return code
	else:
		#print("Result Failed: ",a," + ", b," does not equal 2020.")
		return 0

data = []

with open(input_file) as csvfile:
	data = [float(s) for line in csvfile.readlines() for s in line[:-1].split(' ')]

i = 0
j = 0

for i in data:
	if code != 0:
		break
	j = 0
	for j in data:
		code = CheckSum2020(i,j)
		if code != 0:
			print("The magic code is: ",code, "using ", i, " and ",j)
			break

 