'''
--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
'''

from sys import argv
import string
script, input_file = argv

with open(input_file) as f: 
	contents = f.read() 

groupresponses = contents.split("\n\n")
letters = string.ascii_letters[0:26]

totalYes = 0

for k in groupresponses:
	split = k.split()
	for i in letters:
		countAlpha = 0
		for j in split:
			countAlpha += j.count(i)
		if countAlpha == len(split):
			totalYes += 1

print("Total yes to track: ",totalYes)

