import sys
from Stack import Stack

def reverse_input(stack):
	text = sys.stdin.read().splitlines()
	line = text.pop()
	while line is not None:
		print(line)
		try:
			line = text.pop()
		except IndexError:
			break
