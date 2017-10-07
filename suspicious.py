from sys import argv

argv_one = argv[1] # students
argv_two = argv[2] # delinquents

with open(argv_one) as one, open(argv_two) as two:              # open both text files
	one, two = one.read().splitlines(), two.read().splitlines()	# create two lists
	intersection = sorted(list(set(one)&set(two)))				# check duplicates, put into list, sort
	for line in intersection:									# print one name per line
		print(line)
