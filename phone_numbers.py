line = input()
if line == "!!":
	print("Bye")					# output "Bye" before termination
	exit()

a = {}							# dictionary of names, numbers
while line != "!!":
	split_line = line.split(" ")			# split line on a space
	try:						# try needed due to the following if statement
		if split_line[1] != "?":		# if two strings present, put into dictionary
			a[split_line[0]] = split_line[1]
		elif split_line[1] == "?":
			if split_line[0] in a:
				print("{} has number {}".format(split_line[0], a[split_line[0]]))
			else:
				print("Sorry, there is no {}".format(split_line[0]))
	except IndexError:				# prevents script from crashing if a 'command' isn't inputted
		pass					# continue execution
	line = input()
	if line == "!!":				# this check is also needed inside of the loop,
		print("Bye")				# cause the first check is outside of the loop
