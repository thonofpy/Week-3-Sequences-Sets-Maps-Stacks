num = int(input())
nums = []
solution = []
print("Enter numbers (-1 to end): ", end="")

while num != -1:
	if num in nums:
		solution.append(num)
	else:
		nums.append(num)
	num = int(input())

for num in solution:
	print(str(num) + " ", end="")
print()
