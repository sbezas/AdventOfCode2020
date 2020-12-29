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
	if currentRow != 0:
		if currentCol == 0:
			countOccupied += oldSeating[row][col:col+2].count("X")
		elif currentCol == lastCol:
			countOccupied += oldSeating[row][col-1:col+1].count("X")
		else:
			countOccupied += oldSeating[row][col-1:col+2].count("X")
		#count previous row
	#count current row
	if currentRow < lastRow:
		countOccupied += 1 #placeholder
		#count next row
	return countOccupied

def updateSeat(rowText,currentCol,newSeat):
   return '%s%s%s'%(rowText[:currentCol],newSeat,rowText[currentCol+1:])

oldSeating = contents.split("\n") #file with each row as an element
newSeating = oldSeating

lastRow = len(oldSeating)
lastCol = len(oldSeating[0])

#currentSeat = oldSeating[currentRow,currentCol]
#rowText = oldSeating[currentRow]



#newSeating[currentRow] = updateSeat(rowText,currentCol,newSeat)
#rowText = newSeating[currentRow]
#print(rowText)


currentRow = 0
currentCol = 0
newSeat = ""

'''
# Evaluate and update oldSeating chart to newSeating once
for row in oldSeating:
	print("Processing Row:",currentRow,":",row)
	for col in row:
		currentSeat = col
		countOccupied = 0
		print("Processing row/seat:",currentRow,"/",currentCol,":",currentSeat)
		if currentSeat != ".":
			print("Doing something, is not the floor")
		currentCol += 1
	currentRow += 1
	currentCol = 0'''
	
print("All done!",currentRow,"/",currentCol)
'''
~Loop for full old seating chart !
~Loop for each row !
Look at old seating chart !
Look at row X of old seating chart !
Look at col X of old seating chart !
Save currentSeat to this value "L", "X", or "." !
if "." do nothing and increment !
Determine if change is needed # checkOccupied function
 - look at row -1, col -1 value. if "X" countOccupied += 1
 - look at row -1, col 0 value. if "X" countOccupied += 1
 - look at row -1, col +1 value. if "X" countOccupied += 1
 - look at row 0, col -1 value. if "X" countOccupied += 1 
 - look at row 0, col +1 value. if "X" countOccupied += 1 
 - look at row +1, col -1 value. if "X" countOccupied += 1
 - look at row +1, col 0 value. if "X" countOccupied += 1
 - look at row +1, col +1 value. if "X" countOccupied += 1
if currentSeat == "X" AND countOccupied >= 4:
	newSeat = "L"
	newSeating[currentRow] = updateSeat(rowText,currentCol,newSeat) ## Updates newSeating chart with new value
if currentSeat == "L" AND countOccupied == 0:
	newSeat = "X"
	newSeating[currentRow] = updateSeat(rowText,currentCol,newSeat) ## Updates newSeating chart with new value
currentCol += 1
if currentCol > len(rowText):
	currentCol = 0
	currentRow += 1
if currentRow <= len(oldSeating):
	currentRow += 1
else
	break
~end loop for each row
~end loop for full old seating chart
'''
row = 1
col = 1
print(oldSeating[row-1])
print(oldSeating[row])

