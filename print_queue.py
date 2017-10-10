def print_queue(data, front, back):
	while front is not back:
		item = data[front]
		print(item)
		front = (front + 1) % len(data)
