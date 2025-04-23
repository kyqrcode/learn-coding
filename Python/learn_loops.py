#while loops allows user to execute functions as repeatedly as long as conditions are true
i = 1
while i <= 10:
    print(i)
    i += 1 #or i = i + 1

print("Done with loop")

#for loops allows user to loop through a collection
for chrcter in "Happy Birthday!": #for loops define variable chrcter 
    print(chrcter) #each iteration shows different stored charcter from string

#for loop can be used for arrays, numbers
friends = ["Angel", "Marla", "Moira"]
for friend in friends:
    print(friend)

for index in range(3, 10): #prints out range not included last number
    print(index)

#nested for loops (for loop within a for loop)
grid = [
    [1, 2, 3], #row 0
    [4, 5, 6], #row 1
    [7, 8, 9], #row 2
    [0] #row 3
]

for row in grid:
    for col in row:
        print(col)