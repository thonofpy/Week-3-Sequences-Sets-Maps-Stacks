from Stack import Stack

class Queue:
	def __init__(self):
		self.sorted = Stack()
		self.stack = Stack()

	def isempty(self):
		return self.stack.isempty() and self.sorted.isempty()

	def enqueue(self, item):
		self.stack.push(item)

	def dequeue(self):
		if self.sorted.isempty():
			if self.stack.isempty():
				return None
			else:
				item = self.stack.pop()
				while item is not None:
					self.sorted.push(item)
					try:
						item = self.stack.pop()
					except:
						break
		return self.sorted.pop()
