from sys import argv
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 

bootcode = contents.split("\n")
instructions = bootcode[0] # Line as string
inst = instructions.split() # list of line elements
acc = 0
i = 0
visited = set()
while True:
	print(instructions)
	if i in visited:
		print(acc)
		break
	visited.add(i)
	if inst[0] == "acc":
		acc += int(inst[1])
		i+=1
		instructions = bootcode[i]
		inst = instructions.split()
		continue
	if inst[0] == "jmp":
		i += int(inst[1])
		instructions = bootcode[i]
		inst = instructions.split()
		continue
	if inst[0] == "nop":
		i+=1
		instructions = bootcode[i]
		inst = instructions.split()
		


