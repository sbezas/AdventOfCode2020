'''
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?'''

from sys import argv
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 
	
numbers = contents.split("\n") #file with each row as an element
for i in range(0, len(numbers)): 
    numbers[i] = int(numbers[i]) 
i = 0
j = 25
targetLoc = 25
sumPair = []
workingList = numbers[i:j]
target = numbers[targetLoc]
brokenLoc = 0

def findPair(num1, num2, target):
	if (num1 + num2) == target:
		return True
	else:
		return False

def findRange(workingList,newTarget):
	if sum(workingList) == newTarget:
		return True
	if sum(workingList) > newTarget:
		return "break"
	else:
		return False

num1 = numbers[i]
num2 = numbers[i+1]
target = numbers[targetLoc]
while brokenLoc == 0:
	for num1 in workingList:
		for num2 in workingList:
			sumPair = findPair(num1,num2,target)
			if sumPair == True:
				break
		if sumPair != False:
			#print("Found",target,"using",num1,"and",num2,"at row",targetLoc+1)
			break
	if sumPair == False:
		print("Unable to solve for",target,"using",num1,"and",num2,"row:",targetLoc+1)
		brokenLoc = targetLoc
	i+=1
	j+=1
	targetLoc += 1
	workingList = numbers[i:j]
	target = numbers[targetLoc]

newTarget = numbers[brokenLoc]
print(newTarget)
i=0
j=1
sumRange = False

workingList = numbers[i:j+1]
while findRange(workingList, newTarget) == False:
	for num1 in numbers:	
		for num2 in numbers:
			sumRange = findRange(workingList,newTarget)
			if sumRange == "break":
				break
				j = i
				workingList = numbers[i:j+1]
			elif sumRange == False:
				j += 1
				workingList = numbers[i:j+1]
			elif sumRange == True:
				break
		if sumRange == True:
			break
		else:
			i += 1
		workingList = numbers[i:j+1]
print("Range that sums up to:",newTarget,"is:",workingList)
print("Lower bound:",numbers[i],"Upper Bound:",numbers[j])
print("Sum of range is",sum(workingList))
minVal = min(workingList)
maxVal = max(workingList)
encrpytionWeakness = minVal + maxVal
print("Encryption Weakness is",encrpytionWeakness)
