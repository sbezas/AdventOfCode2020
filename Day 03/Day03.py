from sys import argv
script, input_file = argv

# Navigating Trees Problem

# Use code from previous days to read input.txt file

# Problems to solve
## How to get row to repeat infinitely left to right (or number of rows / number of columns + 1 to the right)
## How to 'view' each row and maintain position to see if a tree is hit

#32 columns (0-31 position)
#323 rows
#duplicate each row 11 times, either up front (larger data set than needed), or some math based on the row #
## leaning toward the second. Can sort out the logic of what 0-31 position I am on depending on the row number. Every 32 iterations will be on the same one. The more I think about it, this is the way to do it, you 'wrap' around the 32 columns....

tmap = []
numTreesHit = 0
with open(input_file) as f:
	tmap = [line.rstrip() for line in f]

numCols = len(tmap[0])-1
print("This is the number of columns: ",numCols, sep='')
numRows = len(tmap)-1
print("This is the number of rows: ", numRows,sep='')
#selecting tmap[y][x] will get a specific coordinate

currentrow = 0 # Remember 0 = Row 1, print statements will be +1, reference values =
currentcol = 0 # Remember 0 = Col 1, print statements will be +1, reference values =

for i in tmap:
	if currentrow == numRows:
		print("All done! Total trees hit:",numTreesHit)
	else:
		print("Approaching next row!")
		if currentrow+1 <10:
			print("Row 0",currentrow+1,": ",tmap[currentrow],sep='')  
		else: 
			print("Row ",currentrow+1,": ",tmap[currentrow],sep='')  
		if currentrow+2 <10:
			print("Row 0",currentrow+2,": ",tmap[currentrow+1],sep='')
		else:
			print("Row ",currentrow+2,": ",tmap[currentrow+1],sep='')
		currentrow += 1
		currentcol += 3
		if currentcol > numCols:
			currentcol += -numCols
		if tmap[currentrow][currentcol] == "#":
			numTreesHit += 1
			print("Ouch! Hit a tree located in column ",currentcol+1,"! That's ",numTreesHit," hit so far!",sep='')
		else:
			print("Just missed the tree located in column ",currentcol+1,"!",sep='')
		print("\n")
