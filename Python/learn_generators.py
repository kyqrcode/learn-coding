import sys

#generator
def firstn_generator(n):
	num = 0
	while num < n:
		yield num
		num += 1

print("generator sum: ", sum(firstn_generator(1000000)))
print("generator size: ",sys.getsizeof(firstn_generator(1000000)))

#compared to a function with a list
def firstn(n):
	nums = []
	num = 0
	while num < n:
		nums.append(num)
		num +=1
	return nums

print("list sum: ", sum(firstn(1000000)))
print("list size: ", sys.getsizeof(firstn(1000000)))

#generators are good for handling or making iterables with large data as it is smaller in size compared to lists