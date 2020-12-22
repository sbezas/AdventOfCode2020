from sys import argv
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 
	
numbers = contents.split("\n") #file with each row as an element
i = 0
j = 25
targetLoc = 25
cannotSolve = 0
sumPair = []
workingList = numbers[i:j]
target = int(numbers[targetLoc])


def findPair(lookingFor, workingList):
	if lookingFor in workingList:
		return True
	else:
		return False

lookingFor = 49
print("Working with: ",workingList)
print("Solving for: ", target)
sumPair = findPair(lookingFor,workingList)
print("Solve using: ", sumPair)


'''
for line in numbers:
		while targetLoc < len(numbers): # Keep the sets at 25
			print("Working with: ",workingList)
			print("Solving for: ", target)
			if findPair(workingList,target) == False:
				cannotSolve = target
				print("Unable to solve for: ",)
			else:
				sumPair = findPair(workingList,target)
				print("Solved using: ", sumPair)
			i+=1
			j+=1
			targetLoc += 1
			workingList = numbers[i:j]
			if targetLoc < len(numbers): # Stop error for accessing out of range
				target = int(numbers[targetLoc])'''
