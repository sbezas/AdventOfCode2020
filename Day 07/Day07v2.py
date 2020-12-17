# Solution from reddit poster : https://www.reddit.com/r/adventofcode/comments/k8a31f/comment/gfvctf4

import re

with open('input.txt',"r") as f:
	lines = f.read().splitlines()
	
bags = {}
bag_count = 0

def has_shiny_gold(color):
	if color == "shiny gold":
		return True
	else:
		return any(has_shiny_gold(c) for _, c in bags[color])

for line in lines:
	color = re.match(r"(.+?) bags contain", line)[1] # Assign the words before bags contain to color
	bags[color] = re.findall(r"(\d+?) (.+?) bags?", line) # For dictionary entry [color] in bags, assign all words starting with the digit up to 'bags' as separate dictionary element

for bag in bags:
	if has_shiny_gold(bag):
		bag_count += 1
	
print("Part 1: " + str(bag_count - 1))

def count_bags(bag_type):
	return 1 + sum(int(number)*count_bags(color) for number, color in bags[bag_type])
	
print("Part 2: " + str(count_bags("shiny gold")-1))
