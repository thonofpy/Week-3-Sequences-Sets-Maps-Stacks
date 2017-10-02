def get_counts(lst):
	counts_lst = [0] * 10
	for word in lst:
		counts_lst[len(word)] += 1
	return counts_lst
