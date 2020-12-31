'''
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?'''

from sys import argv
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 
		
def checkOccupied(currentRow, currentCol, oldSeating, lastRow, lastCol):
	countOccupied = 0
	if currentCol == 0: # If first column, do only count current column and +1
		if currentRow != 0:
			countOccupied += oldSeating[currentRow-1][currentCol:currentCol+2].count("#")
		countOccupied += oldSeating[currentRow][currentCol:currentCol+2].count("#")
		countOccupied -= oldSeating[currentRow][currentCol].count("#")
		if currentRow != lastRow-1:
			countOccupied += oldSeating[currentRow+1][currentCol:currentCol+2].count("#")
	elif currentCol == lastCol: # If last column, only current column and -1
		if currentRow != 0:
			countOccupied += oldSeating[currentRow-1][currentCol-1:currentCol+1].count("#")
		countOccupied += oldSeating[currentRow][currentCol-1:currentCol+1].count("#")
		countOccupied -= oldSeating[currentRow][currentCol].count("#")
		if currentRow != lastRow-1:
			countOccupied += oldSeating[currentRow+1][currentCol-1:currentCol+1].count("#")
	else: # all other columns, count all surrounding cells
		if currentRow != 0:
			countOccupied += oldSeating[currentRow-1][currentCol-1:currentCol+2].count("#")
		countOccupied += oldSeating[currentRow][currentCol-1:currentCol+2].count("#")
		countOccupied -= oldSeating[currentRow][currentCol].count("#")
		if currentRow != lastRow-1:
			countOccupied += oldSeating[currentRow+1][currentCol-1:currentCol+2].count("#")
	return countOccupied

def updateSeat(newRow,currentCol,newSeat):
   return '%s%s%s'%(newRow[:currentCol],newSeat,newRow[currentCol+1:])

# Initial Variables and setup
oldSeating = contents.split("\n") #file with each row as an element
newSeating = oldSeating.copy()
lastRow = len(oldSeating)
lastCol = len(oldSeating[0])
numLoop = 1
numberChanges = 1
numOccupiedSeats = 0

# Evaluate and update oldSeating chart to newSeating once
while numberChanges != 0:
	numberChanges = 0
	currentRow = 0
	currentCol = 0
	newSeat = ""
	countOccupied = 0
	numberChanges = 0
	for row in oldSeating:
#		if currentRow != 0:
#			print("Processing Row:",currentRow-1,":",oldSeating[currentRow-1])
#		print("Processing Row:",currentRow,":",row)
#		if currentRow != lastRow-1:
#			print("Processing Row:",currentRow+1,":",oldSeating[currentRow+1])
		for col in row:
			currentSeat = col
			countOccupied = 0
#			print("Processing row/seat:",currentRow,"/",currentCol,":",currentSeat)
			if currentSeat != ".":
				countOccupied = checkOccupied(currentRow,currentCol,oldSeating,lastRow,lastCol)
#				print("Number of occupied Seats is:",countOccupied)
				if (currentSeat == "L") & (countOccupied == 0):
					newSeat = "#"
					newSeating[currentRow] = updateSeat(newSeating[currentRow], currentCol, newSeat)
					numOccupiedSeats += 1
#					print("Row",currentRow,"was   :",oldSeating[currentRow])
#					print("Row",currentRow,"is now:",newSeating[currentRow])
					numberChanges += 1
				elif (currentSeat == "#") & (countOccupied >= 4):
					newSeat = "L"
					newSeating[currentRow] = updateSeat(newSeating[currentRow], currentCol, newSeat)
					numberChanges += 1
#					print("Row",currentRow,"was   :",oldSeating[currentRow])
#					print("Row",currentRow,"is now:",newSeating[currentRow])
			currentCol += 1
		currentRow += 1
		currentCol = 0
	print("All done with iteration:",numLoop,"Number of changes:",numberChanges)
	numOccupiedSeats = 0
	for i in newSeating:
		numOccupiedSeats += i.count("#")
	print("Number of occupied seats:",numOccupiedSeats)
	if numberChanges == 0:
		print("No changes made! This is iteration:", numLoop)
		break
	else:
		oldSeating = newSeating.copy() # Copy over old with new to begin new comparison
	numLoop += 1
