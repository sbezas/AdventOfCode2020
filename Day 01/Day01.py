from sys import argv

#Psuedo Code logic:
	#Open file, determine number of lines, set check value = 2020, set val1 equal to first line and val2 equal to second line. While i <= max, If val1 = val2, increment val2. Check if val1+val2 = 2020, if yes multiply and return value, print. if no, increment val 2 until val2 location > number of lines. Then increment val 1 and reset val2 to line 1 and repeat.

script, input_file = argv

def CheckSum2020(a,b):
	if a + b = 2020:
		code = a*b
		print("The answer has been found! ",a," and ",b," equal 2020!\n")
		print("Multiplying those together is ",code)
		return 1
	else:
		print("Result Failed: ",a," + ", b," does not equal 2020.")
		return 0



def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print(line_count, f.readline())
	
current_file = open(input_file)

print("First, let's print the whole file\n")
print_all(current_file)

print("Now, let's rewind, kind of like a tape\n")
rewind(current_file)

print('Let\'s print 3 lines!')

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_fil
