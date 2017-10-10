class Stack:
	def __init__(self):
		self.stack = []
		self.top = 0

	def is_empty(self):
		return self.top == 0

	def push(self, item):
		if self.top < len(self.stack):
			self.stack[self.top] = item
		else:
			self.stack.append(item)
		self.top += 1

	def pop(self):
		if self.is_empty():
			return None
		else:
			self.top -= 1
			return self.stack[self.top]

def check_brackets(line):
	brackets= ['()','{}','[]']
	s = Stack()
	for c in line:
		if c in '({[':
			s.push(c)
		elif c in ')}]':
			if(s.is_empty()):
				return False
			if (s.pop() + c) not in brackets:
				return False
	return s.is_empty()
 
check_brackets("()")
