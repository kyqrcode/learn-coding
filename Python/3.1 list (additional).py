num_list = [1, 2, 3, 44, 55, 66, 0, -1,-3 , 2, -2, -11, -22]
print(num_list)

only_list = [num * 2 for num in num_list]
print(only_list)

if_only = [num for num in num_list if num < 0]
print(if_only)

if_else = [num * 11 if num < 0 else num * 0 for num in num_list]
print(if_else)

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
new_prices = [price - 5 for price in prices]

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)