#list can store multiple data values
friends = ["Angel", "Marla", "Moira", "Al", "Rhaj"] #list of strings
numbers = [1, 2, 3] #list of numbers
boolean = [True, False] #list of boolean
#can list mix of strings, numbers, and boolean
#altering lists can be stored as a function


# range can be used to storein a list
count_0to9 = range(10) # range can also be (0, 9)
skips_by_2 = range(2, 9, 2)
print(count_0to9) # output: range(0,10)
print(list(count_0to9)) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(skips_by_2))
#ranges need to be converted to lists first before applying functions like length and print

print("\n")

print(numbers)
print(friends[1]) #should show Marla
#can use negative numbers to grab values starting from the right end
print(friends[1:]) #shows value starting from n: up to the end
print(friends[0:3]) #shows value starting from n: up to before the value position :x
#[:n] start to n
#[-2:] last two elements
#[:-3] all except last 3

print("\n")

#can modify values in list
friends[2] = "Moi"
print(friends[2])

#some common methods and functions for lists
numbers.append(4) #adds new element to the end of the list
print(numbers)
friends.insert(3, "Sam") #inserts new element at the index position stated
print(friends)
numbers.remove(4) #removes an element
print(numbers)
boolean.clear() #removes all elements in the list
print(boolean)
var = numbers.pop() #removes last element of the list OR with index AND can be stored in a variable
print(numbers)
print(var)

print("\n")

friends.sort() #sorts elements in alphabetical order for strings/ascending order for numbers, does not return a value
#sorted(variable): difference is it generates a new list
print(friends)
friends.reverse() #reverses order of list
#friends.sort(reverse=True) for a faster reverse of sorting
print(friends)

print(friends.index("Angel")) #shows the position of the element
#shows ValueError if element is not in the list
print(friends.count("Al")) #counts number of similar chosen elements, should be 1

friends2 = friends.copy() #makes an exact copy of the list
friends2.extend(numbers) #combines data values of lists
print(friends2)

#tuples are similar to lists, most common example is coordinates
coordinates = (4, 5) #tuples cannot be changed/modified (immutable), TypeError if tried to change
#tuples can be stored in a lists
coordinates_list = [(4, 5), (6, 7), (8, 9)]
print(coordinates)
print(coordinates_list)

#2D lists (lists within a list)
grid = [
    [1, 2, 3], #row 0
    [4, 5, 6], #row 1
    [7, 8, 9], #row 2
    [0] #row 3
]
print(grid[0][0]) #should show 1