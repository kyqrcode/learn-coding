array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

sum = 0

for list in array:
    for number in list:
        sum = sum + number
print(sum)

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age <= 21:
    continue
  print(age)