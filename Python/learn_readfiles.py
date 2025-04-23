friends_file = open("C:\[PROJECT] Learn Coding\Python\Read.txt", 'r') #set it up in a variable
# "r" read
# "w" write (overwrites everything)
# "a" append/add on the last
# "r+" read and write

print(friends_file.readable()) #to check if the file is readable
'''
print(friends_file.read()) 
    - prints contents of file

print(friends_file.readline()) 
    - prints first/individual line

print(friends_file.readlines()) 
    -prints each line and put in an array
    - you can do:
        for friend in friends_file.readlines():
            print(employee)
'''

friends_file.close()