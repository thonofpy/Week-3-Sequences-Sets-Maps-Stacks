import sys

def reverse_input(stack):
	lines = sys.stdin.readlines()
	a = []
	for value in lines:
		a.append(value.strip())
	for v in a:
		stack.push(a)
	while not stack.is_empty():
		print(stack.pop().pop())
