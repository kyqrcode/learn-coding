import functools

''' BASICS OF DECORATORS
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
	print("hello")

prints:

before
hello
after
'''

''' Wrapping decorators
def start_end_decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print("start")
		result = func(*args, **kwargs)
		print("end")
		return result
	return wrapper

@start_end_decorator
def add5(x):
	return x + 5

add5 = add5(10)
print(add5)
'''

#Function decorator
def repeat(num_times):
	def decorator_repeat(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(num_times):
				result = func(*args, **kwargs)
			return result
		return wrapper
	return decorator_repeat
		

@repeat(num_times=3)
def greet(name):
	print(f"hello {name}")
	
greet("Ky")

#Stacking decorators on top of each other is also allowed, closest to func gets executd first

#Class decorators
class CountCalls:
	def __init__(self, func):
		self.func = func
		self.num_calls = 0

	def __call__(self, *args, **kwargs): #to implement class decorator
		self.num_calls += 1
		print(f"This function has been executed {self.num_calls} times")
		return self.func(*args, **kwargs)

@CountCalls
def greeting():
	print("Hello")

greeting()
greeting()
greeting()