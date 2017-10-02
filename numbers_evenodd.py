import sys

def get_evenodd_list():
	odd_lst = []
	even_lst = []
	for x in sys.stdin:
		if x == -1:
			break
		elif x % 2 != 0:
			odd_lst.append(x)
		else:
			even_lst.append(x)
	return odd_lst, even_lst
