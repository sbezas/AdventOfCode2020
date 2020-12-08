from sys import argv
script, input_file = argv

tmap = []
numTreesHit = 0
with open(input_file) as f:
	tmap = [line.rstrip() for line in f]

numCols = len(tmap[0])-1
numRows = len(tmap)-1

currentrow = 0 
currentcol = 0 

colincrement = int(input('Enter number of right: '))
rowincrement = int(input('Enter number of down: '))

print("Starting the toboggan run!")
for i in tmap:
	if currentrow == numRows:
		print("All done! Total trees hit:",numTreesHit)
		print("Remember, you went right",colincrement,"and",rowincrement,"down this run.")
		break		
	else:
		if currentrow+1 <10:
			print("Index "," : ",1234567890123456789012345678901,sep='')
			print("Row 0",currentrow+1,": ",tmap[currentrow],sep='')  
		else: 
			print("Index "," : ",1234567890123456789012345678901,sep='')  
			print("Row ",currentrow+1,": ",tmap[currentrow],sep='')  
		if currentrow+2 <10:
			print("Row 0",currentrow+1+rowincrement,": ",tmap[currentrow+rowincrement],sep='')
		else:
			print("Row ",currentrow+1+rowincrement,": ",tmap[currentrow+rowincrement],sep='')
		currentrow += rowincrement
		currentcol += colincrement
		if currentcol > numCols:
			currentcol += - (numCols + 1) ## Need NumCols to equal the number of items, not the last position)
		if tmap[currentrow][currentcol] == "#":
			numTreesHit += 1
			print("Ouch! Hit a tree located in column ",currentcol+1,"! That's ",numTreesHit," hit so far!",sep='')
		else:
			print("Just missed the tree located in column ",currentcol+1,"!",sep='')
		print("\n")
		if currentrow != numRows:
			print("Approaching next row!")
