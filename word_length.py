def get_counts_dict(words):
	d = {}
	for x in words:
		if len(x) not in d:
			d[len(x)] = 1
		else:
			d[len(x)] += 1
	return d
