import sys

#generator
def firstn_generator(n):
	num = 0
	while num < n:
		yield num
		num += 1

print(sum(firstn_generator(1000000)))
print(sys.getsizeof(firstn_generator))

#compared to a function with a list