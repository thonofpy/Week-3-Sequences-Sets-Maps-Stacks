import sys

def get_odd_list():
	odd_lst = []
	for x in sys.stdin:
		if x == -1:
			break
		else:
			if x % 2 != 0:
				odd_lst.append(x)
	return odd_lst

==========================================================
code below is for testing purposes (with hard coded input)
==========================================================
import sys

def get_odd_list():
	lst = [1,2,3,-1,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	odd_lst = []
	for x in lst:
		if x == -1:
			break
		else:
			if x % 2 != 0:
				odd_lst.append(x)
	return odd_lst

def main():
	# call the get_odd_list function and print the result
	odds = get_odd_list()
	print(odds)

if __name__ == "__main__":
	main()
