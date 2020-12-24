'''
--- Part Two ---

To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

The first example above (the one that starts with 16, 10, 15) supports the following arrangements:

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
(The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is 8.

The second example above (the one that starts with 28, 33, 18) has many arrangements. Here are a few:

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)
In total, this set of adapters can connect the charging outlet to your device in 19208 distinct arrangements.

You glance back down at your bag and try to remember why you brought so many adapters; there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?'''

from sys import argv
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 
	
adapters = contents.split("\n") #file with each row as an element
for i in range(0, len(adapters)): 
    adapters[i] = int(adapters[i]) 
adapters = sorted(adapters)
adapters.append(adapters[len(adapters)-1]+3)

num1 = 1 #Starting with 1 for outlet joltage
num2 = 0
num3 = 0 
aLoc = 0
bLoc = 1

print(adapters)

# if diff = 1, num1 += 1, etc.

for i in adapters:
	a = adapters[aLoc]
	b = adapters[bLoc]
	if (b - a) == 1:
		num1 += 1
	elif (b-a) == 2:
		num2 += 1
	elif (b-a) == 3:
		num3 += 1
	aLoc += 1
	bLoc += 1
	if bLoc >= len(adapters):
		break

print("Total 1s:",num1)
print("Total 2s:",num2)
print("Total 3s:",num3)
print("Total joltage difference solution:", num1 * num3)

# Part 2 - Shamelessly stolen from JoseV as I couldn't sort out the right approach. '  https://github.com/davidcbc/aoc/blob/master/2020/python/day10-2.py

steps = [0] * len(adapters)
steps[0] = 1
steps[1] = 1
steps[2] = 2
i=3
while i < len(adapters):
	if adapters[i] - adapters[i-1] <= 3:
		steps[i] += steps[i-1]
	if adapters[i] - adapters[i-2] <= 3:
		steps[i] += steps[i-2]
	if adapters[i] - adapters[i-3] <= 3:
		steps[i] += steps[i-3]
	i += 1

print(steps)
print(steps[len(adapters)-1])
