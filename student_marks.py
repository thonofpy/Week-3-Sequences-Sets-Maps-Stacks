def make_map():
	lines = sys.stdin.readlines()
	d = {}
	try:	# try needed to prevent line 8 from crashing the script
		for x in lines:
			x = x.split()
			d[x[0]] = x[1]
	except IndexError:
		pass
	return d
