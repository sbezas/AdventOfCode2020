'''
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
'''

from sys import argv
script, input_file = argv

rows = 0
cols = 0
seatsBoarded = []

def split_half(a):
    half = len(a) >> 1
    return a[:half], a[half:]

def locateRow(ticketID, rows):
	for i in ticketID:
		if i == "F":
			rows = split_half(rows)
			rows = rows[0]
		elif i == "B":
			rows = split_half(rows)
			rows = rows[1]
		return rows
		
def locateSeat(ticketID, cols):
	for i in ticketID:
		if i == "L":
			cols = split_half(cols)
			cols = cols[0]
		elif i == "R":
			cols = split_half(cols)
			cols = cols[1]
		return cols

def findMySeat(prevSeat, currSeat):
	if currSeat - prevSeat == 1:
		print("Seat Not missing: ", currSeat)
		return 0
	else:
		print("This is your seat! ", currSeat - 1)
		return currSeat - 1

with open(input_file) as f: 
	contents = f.read() 

tickets = contents.split()

highestSeatId = 0
for j in tickets:
	rows = [*range(0,128,1)]
	cols = [*range(0,8,1)]
	for i in j:
		if i == "F" or i == "B":
			rows = locateRow(i, rows)
		elif i == "R" or i == "L":
			cols = locateSeat(i, cols)
	seatID = cols[0] + (rows[0] * 8)
	seatsBoarded.append(seatID)
	if seatID > highestSeatId:
		highestSeatId = seatID
	print("Seat ID: ", seatID)
print("\n")
seatsBoarded.sort()
print("Here's the manifest: ", seatsBoarded)
print("Finished calculating, highest seatID is", highestSeatId)
for i  in seatsBoarded:
	if i == 75:
		print("Ignoring first value")
		prevSeat = i
	else:
		currSeat = i
		mySeat = findMySeat(prevSeat, currSeat)
		if mySeat == 0:
			prevSeat = i
		else:
			print("Found my seat! It is: ", mySeat)
			break	

