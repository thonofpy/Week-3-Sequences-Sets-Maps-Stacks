import sys

def get_odd_list():
	odd_lst = []
	for x in sys.stdin:
		x = int(x)
		if x == -1:
			break
		elif x % 2 != 0:
			odd_lst.append(x)
	return odd_lst
